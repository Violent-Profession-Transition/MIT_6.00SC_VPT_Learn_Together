from lec20_clustering_county import *

#Mammal's teeth example
class Mammal(Point):
    def __init__(self, name, originalAttrs, scaledAttrs = None):
        Point.__init__(self, name, originalAttrs, originalAttrs)
    def scaleFeatures(self, key):
        """overwrite the attrs with scaledFeatures"""
        scaleDict = {'identity': [1,1,1,1,1,1,1,1],
                     '1/max': [1/3.0,1/4.0,1.0,1.0,1/4.0,1/4.0,1/6.0,1/6.0]}
        scaledFeatures = []
        features = self.getOriginalAttrs()
        for i in range(len(features)):
            scaledFeatures.append(features[i]*scaleDict[key][i])
        self.attrs = scaledFeatures
        
def readMammalData(fName):
    """
    return ['Brown Bat', 'Mole', 'Silver Hair Bat', ...]
    and [
      [2.0, 3.0, 1.0, 1.0, 3.0, 3.0, 3.0, 3.0],
      [3.0, 2.0, 1.0, 0.0, 3.0, 3.0, 3.0, 3.0],
      [2.0, 3.0, 1.0, 1.0, 2.0, 3.0, 3.0, 3.0],
    ...]
    """
    dataFile = open(fName, 'r')
    teethList = []
    nameList = []
    for line in dataFile:
        # skip the first line and comment lines
        if len(line) == 0 or line[0] == '#':
            continue
        # Rat 22000066
        dataLine = string.split(line)
        # dataLine = ['Rat', '22000066']
        teeth = dataLine.pop(-1)
        # teeth = '22000066'
        # dataLine is now just ['Rat']
        features = []
        for t in teeth:
            features.append(float(t))
        # features = [2.0,2.0,0.0,0.0...]
        name = ''
        # River Otter         33114312
        # dataLine = ['River', 'Otter']
        for w in dataLine:
            name = name + w + ' '
        name = name[:-1]
        teethList.append(features)
        nameList.append(name)
    return nameList, teethList
    
def buildMammalPoints(fName, scaling):
    """
    get the nameList and featureList from readMammalData
    and return a list of points
    """
    nameList, featureList = readMammalData(fName)
    points = []
    for i in range(len(nameList)):
        point = Mammal(nameList[i], pylab.array(featureList[i]))
        point.scaleFeatures(scaling)
        points.append(point)
    return points

#Use hierarchical clustering for mammals teeth
def test0(numClusters = 2, scaling = 'identity', printSteps = False,
          printHistory = True):
    points = buildMammalPoints('mammalTeeth.txt', scaling)
    cS = ClusterSet(Mammal)
    for p in points:
        cS.add(Cluster([p], Mammal))
    history = cS.mergeN(Cluster.maxLinkageDist, numClusters,
                        toPrint = printSteps)
    if printHistory:
        print ''
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print 'Step', i, 'Merged', names1, 'with', names2
            print ''
    clusters = cS.getClusters()
    print 'Final set of clusters:'
    index = 0
    for c in clusters:
        print '  C' + str(index) + ':', c
        index += 1

def kmeans(points, k, cutoff, pointType, maxIters = 100,
           toPrint = False):
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(points, k)
    clusters = []
    #Create a singleton cluster for each centroid
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while biggestChange >= cutoff and numIters < maxIters:
        #Create a list containing k empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
        for p in points:
            #Find the centroid closest to p
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(k):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add p to the list of points for the appropriate cluster
            newClusters[index].append(p)
        #Update each cluster and record how much the centroid has changed
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            biggestChange = max(biggestChange, change)
        numIters += 1
    #Calculate the coherence of the least coherent cluster
    maxDist = 0.0
    for c in clusters:
        for p in c.members():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Number of iterations =', numIters, 'Max Diameter =', maxDist
    return clusters, maxDist

# use kMeans for mammal clustering
def test1(k = 2, cutoff = 0.0001, numTrials = 1, printSteps = False,
          printHistory = False):
    points = buildMammalPoints('mammalTeeth.txt', '1/max')
    if printSteps:
        print 'Points:'
        for p in points:
            attrs = p.getOriginalAttrs()
            for i in range(len(attrs)):
                attrs[i] = round(attrs[i], 2)
            print '  ', p, attrs
    numClusterings = 0
    bestDiameter = None
    while numClusterings < numTrials:
        clusters, maxDiameter = kmeans(points, k, cutoff, Mammal)
        if bestDiameter == None or maxDiameter < bestDiameter:
            bestDiameter = maxDiameter
            bestClustering = copy.deepcopy(clusters)
        if printHistory:
            print 'Clusters:'
            for i in range(len(clusters)):
                print '  C' + str(i) + ':', clusters[i]
        numClusterings += 1
    print '\nBest Clustering'
    for i in range(len(bestClustering)):
        print '  C' + str(i) + ':', bestClustering[i]


if __name__ == "__main__":
    # unit test for Point class
    p_Rat = Point("Rat", [1,2,3])
    assert p_Rat.dimensionality() == 3
    assert p_Rat.toStr() == 'Rat[1, 2, 3]'
    p_Monkey = Point("Monkey", [3,2,1])
    assert p_Rat.distance(p_Monkey) > 2.82

    # unit test for Cluster class
    p_River_Otter = Mammal("River Otter", [3.0, 3.0, 1.0, 1.0, 4.0, 3.0, 1.0, 2.0])
    p_Dog = Mammal("Dog", [3.0, 3.0, 1.0, 1.0, 4.0, 4.0, 2.0, 3.0])
    p_Brown_Bat = Mammal("Brown Bat", [2.0, 3.0, 1.0, 1.0, 3.0, 3.0, 3.0, 3.0])
    c_1 = Cluster([p_River_Otter], Point)
    assert c_1.toStr() == "River Otter[3.0, 3.0, 1.0, 1.0, 4.0, 3.0, 1.0, 2.0]"
    c_2 = Cluster([p_Dog], Mammal)
    c_3 = Cluster([p_Brown_Bat], Mammal)
    assert c_1.isIn("River Otter")
    assert c_2.isIn("Dog")
    c_3_centroid = c_3.getCentroid()
    assert c_3_centroid.toStr() == "mean[ 2.  3.  1.  1.  3.  3.  3.  3.]"

    # unit test for ClusterSet class
    cS_1 = ClusterSet(Mammal)
    cS_1.add(c_1)
    assert cS_1.__str__() == "River Otter\n"
    cS_1.add(c_2)
    assert cS_1.__str__() == "River Otter\nDog\n"
    #cS_1.mergeClusters(c_1, c_2)
    #assert cS_1.__str__() == "Dog, River Otter\n"
    cS_1.add(c_3)
    cS_1.mergeOne(Cluster.singleLinkageDist, toPrint=True)
    cS_1.mergeOne(Cluster.singleLinkageDist, toPrint=True)
    cS_1.mergeOne(Cluster.singleLinkageDist, toPrint=True)

    # test hierarchical clustering
    #test0(numClusters=10)

    # test k-means clustering
    test1()