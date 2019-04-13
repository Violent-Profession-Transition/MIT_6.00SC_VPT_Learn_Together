import random
import pylab

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

def poll(n, p):
    """
    p is percentage in the sampled
    n is sample size
    conduct poll
    """
    votes = 0.0
    for i in range(n):
        if random.random() < p/100.0:
            votes += 1
    return votes

def TestError(n=1000, p=46.0, numTrials=10000):
    """
    p is the percentage of vote candidate XYZ is going to get
    run 10k trials,
    each trial poll 1000 people
    """
    results = []
    for t in range(numTrials):
        results.append(poll(n,p))
    print("relative SD: ", str((stdDev(results)/n)*100), "%")
    results = pylab.array(results)/n
    pylab.hist(results)
    pylab.xlabel("Fraction of Votes")
    pylab.ylabel("Number of polls")

TestError()
pylab.show()