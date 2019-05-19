import pylab, random, string, copy, math


class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        difference = self.attrs - other.attrs
        return sum(difference * difference) ** 0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name


class County(Point):
    weights = pylab.array([1.0] * 14)

    # Override Point.distance to use County.weights to decide the
    # significance of each dimension
    def distance(self, other):
        difference = self.getAttrs() - other.getAttrs()
        return sum(County.weights * difference * difference) ** 0.5


class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        meanPoint = self.pointType(
            'mean',
            totVals/float(len(self.points)),
            totVals/float(len(self.points)))
        return meanPoint
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def getPoints(self):
        return self.points
    def contains(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __str__(self):
        result = ''
        for p in self.points:
            result = result + str(p) + ', '
        return result[:-2]
    def isIn(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False


def kmeans(points, k, cutoff, pointType, minIters = 3, maxIters = 100, toPrint = False):
    """ Returns (Cluster list, max dist of any point to its cluster) """
    #Uses random initial centroids
    initialCentroids = random.sample(points,k)
    clusters = []
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while (biggestChange >= cutoff and numIters < maxIters) or numIters < minIters:
        print "Starting iteration " + str(numIters)
        newClusters = []
        for c in clusters:
            newClusters.append([])
        for p in points:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(p)
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            #print "Cluster " + str(i) + ": " + str(len(clusters[i].points))
            biggestChange = max(biggestChange, change)
        numIters += 1
        if toPrint:
            print 'Iteration count =', numIters
    maxDist = 0.0
    for c in clusters:
        for p in c.getPoints():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Total Number of iterations =', numIters, 'Max Diameter =', maxDist
    print "biggestChange is: ", biggestChange
    return clusters, maxDist

#US Counties example
def readCountyData(fName, numEntries = 14):
    dataFile = open(fName, 'r')
    dataList = []
    nameList = []
    maxVals = pylab.array([0.0]*numEntries)
    #Build unnormalized feature vector
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        name = dataLine[0] + dataLine[1]
        features = []
        #Build vector with numEntries features
        for f in dataLine[2:]:
            try:
                f = float(f)
                features.append(f)
                if f > maxVals[len(features)-1]:
                    maxVals[len(features)-1] = f
            except ValueError:
                name = name + f
        if len(features) != numEntries:
            print "line data incomplete, discard", line
            continue
        dataList.append(features)
        nameList.append(name)
    return nameList, dataList, maxVals

def buildCountyPoints(fName):
    """
    Given an input filename, reads County values from the file and returns
    them all in a list.
    """
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        normalizedAttrs = originalAttrs/pylab.array(maxVals)
        points.append(County(nameList[i], originalAttrs, normalizedAttrs))
    return points

def randomPartition(l, p):
    """
    Splits the input list into two partitions, where each element of l is
    in the first partition with probability p and the second one with
    probability (1.0 - p).

    l: The list to split
    p: The probability that an element of l will be in the first partition

    Returns: a tuple of lists, containing the elements of the first and
    second partitions.
    """
    l1 = []
    l2 = []
    for x in l:
        if random.random() < p:
            l1.append(x)
        else:
            l2.append(x)
    return (l1,l2)

def getAveIncome(cluster):
    """
    Given a Cluster object, finds the average income field over the members
    of that cluster.

    cluster: the Cluster object to check

    Returns: a float representing the computed average income value
    """
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[1]

    return float(tot) / len(cluster.getPoints())


def test(points, k = 200, cutoff = 0.1):
    """
    A sample function to show you how to do a simple kmeans run and graph
    the results.
    """
    incomes = []
    print ''
    clusters, maxSmallest = kmeans(points, k, cutoff, County)

    for i in range(len(clusters)):
        if len(clusters[i].points) == 0: continue
        incomes.append(getAveIncome(clusters[i]))

    pylab.hist(incomes)
    pylab.xlabel('Ave. Income')
    pylab.ylabel('Number of Clusters')
    pylab.show()

# all the data in counties.txt
points = buildCountyPoints('counties.txt') # points is a list
# only a tenth of the full data
# random.seed(123)
testPoints = random.sample(points, len(points)/10)

# Problem 0 Provided classes and functions
# Point Class: represent the data points
# County Class: Extends Point class.
#   represent the counties and
#   contains a method that returns the distance between two Counties
# Cluster Class: represent the clusters
# kmeans() -> return
#   clusters,
#   maxDist (worst cluster point to its centroid)
# readCountyData() -> return
#   nameList, (list of the names like CASanFrancis)
#   dataList (list of feature vectors),
#   maxVals (dynamic range of the feature vector)
# buildCountyData() -> return
#   list of normalized Counties based on readCountyData()
# randomPartition() partitions a list into two lists

# test
#test(testPoints, k=300)

# Problem 1 Graph Removed Error
 
def graphRemovedErr(points, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Should produce graphs of the error in training and holdout point sets, and
    the ratio of the error of the points, after clustering for the given values of k.
    """
    # Partition your data set into a training and holdout set, 
    # where the holdout set should be 20% of all the points.
    (training, holdout) = randomPartition(points, 0.8)
    # find the total error of the training set
    tot_error_training = []
    tot_error_holdout = []
    for k in kvals:
        tot_error = 0.0
        (clusters, maxDist) = kmeans(training, k, cutoff, County)
        for c in clusters:
            for p in c.getPoints():
                tot_error += (p.distance(c.getCentroid()))**2
        tot_error_training.append(tot_error)
        # Given the holdout set, find the error by calculating 
        # the squared distance of each point in the holdout set
        # to its nearest cluster.
        holdout_error = 0.0
        for p in holdout:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            # find the closest cluster
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            holdout_error += smallestDistance**2
        tot_error_holdout.append(holdout_error)
    pylab.plot(kvals, tot_error_training, label="Training-set Error")
    pylab.plot(kvals, tot_error_holdout, label="Holdout-set Error")
    pylab.xlabel('Number of clusters [K value]')
    pylab.ylabel('Value of Total Error')
    pylab.title("Error vs K")
    pylab.legend(loc='best')
    pylab.show()
        
    print tot_error_training
    print tot_error_holdout

    # also graph the ratio of the error of the holdout set
    # over the total error of the training set
    ratio_t_h = []
    for i in range(len(tot_error_training)):
        ratio_t_h.append(
            tot_error_holdout[i] / tot_error_training[i]
        )
    pylab.plot(kvals, ratio_t_h, label="Ratio of Holdout/Training Total Error")
    pylab.xlabel('Number of clusters [K value]')
    pylab.ylabel('Ratio of holdout/training total error')
    pylab.title("Error Ratio vs K")
    pylab.legend(loc='best')
    pylab.show()

# graph using the whole county dataset
# graphRemovedErr(points)

# Problem 2 k-means and my county
# run k=50 three times
# my county is Rice in Minnesota where St Olafs College is!
# MNRice
def run_kMeans(k = 50, cutoff = 0.01, numTrials = 1, myHome = 'NYNewYork'):
    #Build the set of points
    points = buildCountyPoints('counties.txt')
    # display the points on screen
    print 'Num of Points: ', len(points)
    # for p in points:
    #     attrs = p.getAttrs()
    #     for i in range(len(attrs)):
    #         attrs[i] = round(attrs[i], 2)
    #     print '  ', p, attrs
    # prepare for k-means
    numClusterings = 0
    bestDistance = None
    #Run k-means multiple times and choose best
    while numClusterings < numTrials:
        print 'Starting clustering number', numClusterings
        clusters, maxSmallest = kmeans(points, k, cutoff, County)
        numClusterings += 1
        if bestDistance == None or maxSmallest < bestDistance:
            bestDistance = maxSmallest
            bestClustering = copy.deepcopy(clusters)
        print 'Clusters:'
        for i in range(len(clusters)):
            print '  C' + str(i) + ':', len(clusters[i].points)
    print '\nBest Clustering'
    for i in range(len(bestClustering)):
        print '  C' + str(i) + ':', len(bestClustering[i].points)
    for c in bestClustering:
        if c.isIn(myHome):
            print '\nHome Cluster:', c, bestClustering.index(c)
            print 'Ave. income =', round(getAveIncome(c),0)

#run_kMeans()

# Problem 3 Graphing Prediction Error
# cluster a training set and examine the error if the clusters
# were used to classify the holdout set

def graphPredictionErr(points, dimension, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Given input points and a dimension to predict, should cluster on the
    appropriate values of k and graph the error in the resulting predictions,
    """
    # reset the weights
    County.weights = pylab.array([1.0] * 14)
    # Set the weight of the Poverty feature to 0
    #County.weights[2] = 0.0

    # change another feature in the feature dimention
    for d in dimension:
        County.weights[d] = 0.0

    print "County.weights is: ", County.weights

    # Partition your data set into a training and holdout set, 
    # where the holdout set should be 20% of all the points.
    (training, holdout) = randomPartition(points, 0.8)
    tot_error_holdout = []
    for k in kvals:
        tot_diff_error = 0.0
        (clusters, maxDist) = kmeans(training, k, cutoff, County)
        print "<<<<< now try with holdout set >>>>>"
        # Given the holdout set, find the closest cluster
        for p in holdout:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            # find the closest cluster for p
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            # closest cluster c to p is:
            c = clusters[index]
            if c.getPoints() == []:
                print "c is empty!"
                continue
            print "closest cluster c to p is: ", c
            # find the average POVERTY of c
            tot_poverty_c = 0.0
            for mem in c.getPoints():
                tot_poverty_c += mem.getOriginalAttrs()[2]
                print "c's point has povety of: ", mem.getOriginalAttrs()[2]
            avg_poverty_c = tot_poverty_c / len(c.getPoints())
            print "Average poverty of closest cluster c to p is: ", avg_poverty_c, "for p: ", p
            # the actual p's poverty
            actual_poverty_p = p.getOriginalAttrs()[2]
            tot_diff_error += (actual_poverty_p - avg_poverty_c)**2
        tot_error_holdout.append(tot_diff_error)

    print tot_error_holdout

    pylab.plot(kvals, tot_error_holdout, "bo", label="Diff p-poverty subtract avg-poverty")
    pylab.xlabel('Number of clusters [K value]')
    pylab.ylabel('Value of Diff p-poverty avg-poverty')
    #pylab.ylim([0,20000])
    pylab.title("Predicted Error vs K using empty dimension {}".format(dimension))
    pylab.legend(loc='best')
    pylab.show()

# test problem 3 just poverty = 0
#graphPredictionErr(testPoints, [0,1,3,4,5,6,7,8,9,10,11,12,13])
#graphPredictionErr(testPoints, [2])

# problem 4
# try using empty xxx
def PredictionErr(points, dimension, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Given input points and a dimension to predict, should cluster on the
    appropriate values of k and graph the error in the resulting predictions,
    """
    # reset the weights
    County.weights = pylab.array([1.0] * 14)
    # Set the weight of the Poverty feature to 0
    #County.weights[2] = 0.0

    # change another feature in the feature dimention
    for d in dimension:
        County.weights[d] = 0.0

    print "County.weights is: ", County.weights

    # Partition your data set into a training and holdout set, 
    # where the holdout set should be 20% of all the points.
    (training, holdout) = randomPartition(points, 0.8)
    tot_error_holdout = []
    for k in kvals:
        print "+++++++++++++++++++++++++++++++ new K", k
        tot_diff_error = 0.0
        (clusters, maxDist) = kmeans(training, k, cutoff, County)
        #print "<<<<< now try with holdout set >>>>>"
        # Given the holdout set, find the closest cluster
        for p in holdout:
            print "For p: ", p
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            # find the closest cluster for p
            for i in range(len(clusters)):
                print "clusters ",i, clusters[i]
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            print "index is: ", index
            # closest cluster c to p is:
            c = clusters[index]
            print "closest cluster c to p is: ", c
            if c.getPoints() == []:
                print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^c is empty!"
                assert False
            # find the average POVERTY of c
            tot_poverty_c = 0.0
            for mem in c.getPoints():
                tot_poverty_c += mem.getOriginalAttrs()[2]
                #print "c's point has povety of: ", mem.getOriginalAttrs()[2]
            avg_poverty_c = tot_poverty_c / len(c.getPoints())
            #print "Average poverty of closest cluster c to p is: ", avg_poverty_c, "for p: ", p
            # the actual p's poverty
            actual_poverty_p = p.getOriginalAttrs()[2]
            tot_diff_error += (actual_poverty_p - avg_poverty_c)**2
        tot_error_holdout.append(tot_diff_error)

    print "))))))))))))))))))))))))", sum(tot_error_holdout)

PredictionErr(testPoints, [0,1,3,4,5,6,7,8,9,10,11,12,13])

"""
0   HomeValue2000
1   Income1999
2   Poverty1999
3   PopDensity2000
4   PopChange
5   Prcnt65+
6   Below18
7   PrcntFemale2000
8   PrcntHSgrads2000
9   PrcntCollege2000
10  Unemployed
11  PrcntBelow18
12  LifeExpectancy
13  FarmAcres
"""

#PredictionErr(testPoints, [0,1,3,4,5,6,7,8,9,10,11,12,13]) # 47.8977515112
#PredictionErr(testPoints, [2]) # 8104.53995325
#PredictionErr(testPoints, [0,1,2]) # 11590
#PredictionErr(testPoints, [0,1,2,3]) # 8889
#PredictionErr(testPoints, [0,1,2,3,4]) # 6125
#PredictionErr(testPoints, [2,13]) # 3785!!
#PredictionErr(testPoints, [2,11,13]) # 9348
#PredictionErr(testPoints, [2,3,4,13]) # 5562
#PredictionErr(testPoints, [2,3,4,5,13]) # 6805
#PredictionErr(testPoints, [2,3,4,5,6,13]) # 6405
#PredictionErr(testPoints, [2,3,4,7,13]) # 7266
#PredictionErr(testPoints, [2,3,4,8,13]) # 9316
#PredictionErr(testPoints, [2,3,4,9,13]) # 5201
#PredictionErr(testPoints, [2,3,4,10,13]) # 8720
#PredictionErr(testPoints, [2,3,4,11,13]) # 3572!!
#PredictionErr(testPoints, [2,3,4,12,13]) # 6446
#PredictionErr(testPoints, [2,3,11,13]) # 9428
#PredictionErr(testPoints, [2,4,11,13]) # 9121
#PredictionErr(testPoints, [2,3,4,5,6,7,8,9,11,13]) # 4517

# graphPredictionErr(points, [2])
# graphPredictionErr(points, [2,13])
# graphPredictionErr(points, [2,3,4,13])
# graphPredictionErr(points, [2,3,4,9,13])
# graphPredictionErr(points, [2,3,4,11,13])
# graphPredictionErr(points, [2,3,4,5,6,7,8,9,11,13])