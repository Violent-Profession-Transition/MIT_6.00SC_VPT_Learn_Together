import random, pylab


L = [1,1,1,1,2]
# normal histgram without weight
pylab.hist(L, hatch="+")

# the weight is the percentage relative to the total number of appearances
factor = pylab.array(len(L)*[1])/len(L)
print(factor)
# [0.2, 0.2, 0.2, 0.2, 0.2]

pylab.figure()

pylab.hist(L, weights=factor, hatch="/")
pylab.figure()

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

def plotMeans(numDice, numRolls, numBins, legend, color, style):
    """
    numDice: int number of Dice rolled in one go
    numRolls: int how many rolls in total
    """
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means),
               hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1, 1000000, 200, '1 die', 'b', '*')
print('Mean of rolling 1 continuous-die =', str(mean) + ',', 'Std =', std)

mean, std = plotMeans(50, 1000000, 200, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 continuous-dice =', str(mean) + ',', 'Std =', std)

pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()

pylab.show()

