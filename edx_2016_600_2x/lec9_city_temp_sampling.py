import pylab, numpy, random


def makeHist(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

def getHighs():
    """read the lines in the csv file
    CITY,TEMP,DATE
    SEATTLE,3.1,19610101
    SEATTLE,0.55,19610102
    SEATTLE,0,19,...
    """
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    return population

def getMeansAndSDs(population, sample, verbose=False):
    """
    verbose mode will produce histograms
    """
    popMean = sum(population) / len(population)
    sampleMean = sum(sample) / len(sample)
    if verbose:
        makeHist(population,
                'Daily High 1961-2015, population (mean = {})'.format(round(popMean, 2)),
                'Degrees C',
                'Number of Days')
        pylab.figure()
        makeHist(sample,
                'Daily High 1961-2015, Sample of size {} (mean = {})'.format(len(sample), round(sampleMean, 2)),
                'Degrees C',
                'Number of Days')
        print("Population Mean =", popMean)
        print("Population Standard Deviation =", numpy.std(population))
        print("Sample Mean =", sampleMean)
        print("Sample Standard Deviation =", numpy.std(sample))
    return popMean, sampleMean, numpy.std(population), numpy.std(sample)

random.seed(0)
population = getHighs()
sampleSize = 100  # sample size = 100
numSamples = 1000  # do sampling 1000 times

maxMeanDiff = 0
maxSDDiff = 0

sampleMeans = []

for i in range(numSamples):
    print("trying on ", i, "th sampling")
    sample = random.sample(population, sampleSize)
    # sample without replacement
    samplingResult = getMeansAndSDs(population, sample)
    popMean = samplingResult[0]
    sampleMean = samplingResult[1]
    popSD = samplingResult[2]
    sampleSD = samplingResult[3]
    # gather all the sampleMeans
    sampleMeans.append(sampleMean)

    if abs(popMean - sampleMean) > maxMeanDiff:
        maxMeanDiff = abs(popMean - sampleMean)
    if abs(popSD - sampleSD) > maxSDDiff:
        maxSDDiff = abs(popSD - sampleSD)
# after numSamples samplings:
print("mean of sample Means =", round(sum(sampleMeans)/len(sampleMeans), 2))
print("SD of sample means =", round(numpy.std(sampleMeans), 2))
print("Maximum difference in means =", round(maxMeanDiff, 2))
print("Maximum difference in Standard Deviations =", round(maxSDDiff, 2))

# plot the histogram, since getMeansAndSDs's verbose is off
makeHist(sampleMeans, "Means of Samples", "Mean", "Frequency")
pylab.axvline(x=popMean, color="r")
pylab.figure()


def showErrorBars(population, sizes, numTrials):
    sizeMeans, sizeSDs = [], []
    popMean = sum(population)/len(population)

    for sampleSize in sizes:
        sampleMeans = []
        for i in range(numTrials):
            print("trying on ", i, "th trial, on size:", sampleSize)
            sample = random.sample(population, sampleSize)
            # sample without replacement
            samplingResult = getMeansAndSDs(population, sample)
            sampleMean = samplingResult[1]
            # gather all the sampleMeans
            sampleMeans.append(sampleMean)
        mean_i = round(sum(sampleMeans)/len(sampleMeans), 2)
        sd_i = round(numpy.std(sampleMeans), 2)
        sizeMeans.append(mean_i)
        sizeSDs.append(sd_i)

    pylab.errorbar(
            sizes,
            sizeMeans,
            yerr=1.96*pylab.array(sizeSDs),
            fmt='o',
            label='95% Confidence Interval')

    pylab.axhline(popMean, color="r", label="Population Mean")
    pylab.title("Mean Temperature (50 trials)")
    pylab.xlabel("Sample Size")
    pylab.ylabel("Mean")
    pylab.legend(loc="best")


showErrorBars(population, [50,100,200,300,400,500,600], 50)

def sem(SD, size):
    return SD / (size)**0.5

### Testing the SEM
random.seed(0)
sampleSizes = (25,50,100,200,300,400,500,600)
numTrials = 50
population = getHighs()
popSD = numpy.std(population)
sems = []
sampleSDs = []
for size in sampleSizes:
    sems.append(sem(popSD, size))
    means = []
    for t in range(numTrials):
        sample = random.sample(population, size)
        means.append(sum(sample)/len(sample))
    # sampleSD for that sampleSize after t trials
    sampleSDs.append(numpy.std(means))

# plot the SEM
pylab.figure()
pylab.plot(sampleSizes, sampleSDs, label="actual SD of 50 Trials")
pylab.plot(sampleSizes, sems, 'r--', label="SEM")
pylab.title("SEM vs SD for 50 Trials")
pylab.legend()

pylab.show()
