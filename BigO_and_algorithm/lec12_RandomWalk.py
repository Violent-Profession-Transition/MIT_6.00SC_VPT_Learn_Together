import random


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        # it returns a new instance of a Location
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFrom(self, other):
        other_x = other.x
        other_y = other.y
        xDist = self.x - other_x
        yDist = self.y - other_y
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        # print location
        return "({}, {})".format(self.x, self.y)

class Field(object):
    """maps drunks to location
    it is a collection of drunk and locations"""
    def __init__(self):
        """help us keep track of drunks"""
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            return ValueError("Duplicate drunk")
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
    def getLoc(self, drunk):
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [ (0,1), (0,-1), (1,0), (-1,0) ]
        return random.choice(stepChoices)
    def __str__(self):
        return "drunk with name: " + self.name

def walk(field, drunk, numSteps):
    start = field.getLoc(drunk)
    for step in range(numSteps):
        field.moveDrunk(drunk)
    return start.distanceFrom(field.getLoc(drunk))

def simuWalks(numSteps, numTrials):
    homer = Drunk("Homer")
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances
