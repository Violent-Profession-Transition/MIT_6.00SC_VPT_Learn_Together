import random, pylab


#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


class Location:
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(
                self.x + deltaX,
                self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        """return Euclidean distance
        from two Locations"""
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return "<{},{}>".format(self.x, self.y)


class Field:
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        self.drunks[drunk] = loc
    def getLoc(self, drunk):
        """return the Location value
        of a Drunk in self.drunks"""
        return self.drunks[drunk]
    def moveDrunk(self, drunk):
        # Drunk's method takeStep
        xDist, yDist = drunk.takeStep()
        # currentLocation is Location
        currentLocation = self.drunks[drunk]
        # use move method of Location to
        # get to a new Location
        self.drunks[drunk] = \
                currentLocation.move(xDist, yDist)


class Drunk:
    def __init__(self, name = "Homer"):
        self.name = name
    def __str__(self):
        return 'Drunk Name: ' + self.name
    def takeStep(self):
        raise NotImplementedError


# two subclasses of Drunk
class UsualDrunk(Drunk):
    """the usual drunk wonders around at random"""
    def takeStep(self):
        return random.choice(
                 [
                   (0.0, 1.0),
                   (0.0, -1.0),
                   (1.0, 0.0),
                   (-1.0, 0.0) ])


class ColdDrunk(Drunk):
    """the i hate winter drunk who tries to move southward"""
    def takeStep(self):
        return random.choice(
                 [
                   (0.0, 0.9), # not willing to go North
                   (0.0, -1.1),# more willing to go South
                   (1.0, 0.0),
                   (-1.0, 0.0) ])


class PolarBearDrunk(Drunk):
    """drunk polar bear that moves randomly along x y,
    taking larger steps when moving South, smaller steps moving North"""
    def takeStep(self):
        directionList = [
                (0.0, 0.5),
                (1.0, 0.0),
                (-1.0, 0.0),
                (0.0, -1.5)]
        return random.choice(directionList)


###### Simulation ######

# Simulating a single Walk
def walk(f, d, numSteps):
    """
    f: Field
    d: Drunk
    numSteps: int >= 0
    move Drunk d numSteps times;
    return: distance between final and start Loc
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

# Simulating Multiple Walks
def simWalks(numSteps, numTrials, dClass):
    """
    numSteps: int >= 0
    numTrials: int > 0
    dClass: subclass of Drunk
    -----
    Simulates numTrials Walks of numSteps steps
    return: list of distances from each trial
    """
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        # reset the Field for each trial
        f = Field()
        f.addDrunk(Homer, origin)
        # do a walk, save to the distances list
        distances.append(round(
            walk(
                f,
                Homer,
                numSteps
            ), 1
        ))
    return distances

# run the simulations
def simDrunk(numTrials, dClass, walkLengths):
    """
    walkLengths: tuple of ints >= 0
    numTrials: int > 0
    dClass: subclass of Drunk
    -----
    for each numSteps in walkLengths,
    run simWalks with numTrials walks
    return a list of meanDistances for walkLengths
    """
    meanDistances = []
    for numSteps in walkLengths:
        print(dClass.__name__, "random walk of", numSteps, "steps did", numTrials, "walks" )
        distances = simWalks(
              numSteps, numTrials, dClass
            )
        mean = round(sum(distances)/len(distances), 2)
        #  print("Mean =", mean)
        #  print("Max =", max(distances))
        #  print("Min =", min(distances))
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    """
    run simDrunk based on the dClass in drunkKinds
    and plot the graph
    """
    index = 0
    #  styleChoice = ['m-', 'b--', 'g-.']
    styleChoice = ['m+', 'b^', 'go']
    for dClass in drunkKinds:
        curStyle = styleChoice[index]
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
        index += 1
    pylab.title("Mean Distance from Origin ({} trials)".format(numTrials))
    pylab.xlabel("Number of Steps")
    pylab.ylabel("Distance from Origin")
    pylab.legend(loc='best')

#  random.seed(0)
#  numSteps = [x for x in range(10,1000,10)]
#  simAll((UsualDrunk, ColdDrunk, PolarBearDrunk), numSteps, 100)
#  pylab.show()

# plot the Locations
def getFinalLocs(numSteps, numTrials, dClass):
    """return a list of Locations"""
    Homer = dClass()
    origin = Location(0,0)
    locs = []
    for t in range(numTrials):
        print(dClass.__name__, "random walk of", numSteps, "steps", t, "th walk" )
        # reset the Field for each trial
        f = Field()
        f.addDrunk(Homer, origin)
        # do a walk, save to the distances list
        # but only save the final location
        for s in range(numSteps):
            f.moveDrunk(Homer)
        locs.append(f.getLoc(Homer))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    """
    gather the Locs from Walks,
    calculate meanX and meanY,
    and plot all final Locs X, Y
    """
    styleChoice = ('k+', 'r^', 'mo')
    index = 0
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals = [loc.getX() for loc in locs]
        yVals = [loc.getY() for loc in locs]
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(xVals) / len(xVals)
        meanY = sum(yVals) / len(yVals)
        curStyle = styleChoice[index]
        pylab.plot(xVals, yVals, curStyle,
                label=dClass.__name__ + " mean location = <{}, {}>".format(round(meanX,2), round(meanY,2)))
        index += 1
    pylab.title("Location at End of Walks ({} steps for {} walks)".format(numSteps, numTrials))
    #  pylab.ylim(-3000, 3000)
    #  pylab.xlim(-3000, 3000)
    pylab.xlabel("Steps East/West of Origin")
    pylab.ylabel("Steps North/South of Origin")
    pylab.legend(loc="upper left")


random.seed(0)
#  plotLocs((UsualDrunk, ColdDrunk, PolarBearDrunk), 1000, 10000)
plotLocs((ColdDrunk,), 1000, 10000)
pylab.show()


# plot the trajectory of Drunk
def traceWalk(numSteps):
    """
    trace the locs for each step in numSteps
    only one walk
    """
    print("Random walk of", numSteps, "steps")
    d = UsualDrunk()
    f = Field()
    # init the field with a drunk
    f.addDrunk(d, Location(0,0))
    snapshots = []
    for step in range(numSteps):
        f.moveDrunk(d)
        snapshots.append(f.getLoc(d))
    # after completion of the walk
    xVals = [loc.getX() for loc in snapshots]
    yVals = [loc.getY() for loc in snapshots]
    pylab.plot(xVals, yVals, "b-", label="UsualDrunk trajectory")
    pylab.title("Trajectory of Walk ({} steps)".format(numSteps))
    pylab.xlabel("Steps East/West of Origin")
    pylab.ylabel("Steps North/South of Origin")
    pylab.legend(loc="upper left")

#  random.seed(0)
#  traceWalk(10000)
#  pylab.show()
