import random, pylab

"""
number of needles in Circle = num_C
number of needles in whole Square = num_S
pi/4 = num_C/num_S
pi = 4*num_C/num_S
"""

class Circle:
    """circle = x**2 + y**2 = 1"""
    def __str__(self):
        return "Circle of radius 1"
    def inside_Circle(self, Coordinate):
        y_bound = 1 - (Coordinate.x)**2
        return (Coordinate.y)**2 <= y_bound
        

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

circle = Circle()

def stdDev(X):
    """
    calculates standard deviation,
    based on a list X
    """
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    return (tot/len(X))**0.5


def simulatePI(num_S):
    global circle
    num_C = 0.0
    for i in xrange(num_S):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        random_point = Coordinate(x,y)
        if circle.inside_Circle(random_point):
            num_C += 1

    print("PI is: ", 4*num_C/num_S)
    return 4*num_C/num_S

def runTrials(numTrials=10, num_S=1000):
    results = []
    for i in xrange(numTrials):
        results.append(simulatePI(num_S))
    return results
 

def estimatePI(numTrials, num_S, precision):
    estimates = runTrials(numTrials, num_S)
    while stdDev(estimates) > precision:
        num_S *= 2
        estimates = runTrials(numTrials, num_S)
        print("now SD is: ", stdDev(estimates))
        print("num_S is now: ", num_S)
    mean_PI = sum(estimates)/float(len(estimates))
    print("mean PI is: ", mean_PI)

estimatePI(20, 1000, 0.01/4)

# ('now SD is: ', 0.0019763776392679247)
# ('num_S is now: ', 512000)
# ('mean PI is: ', 3.141096484375)