#Code shared across examples
import pylab, random, string, copy

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        if normalizedAttrs == None:
            self.attrs = originalAttrs
        else:
            self.attrs = normalizedAttrs
    def dimensionality(self):
        """dimentionality is the length of attrs array"""
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        # for all the features in the dimensionality
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i])**2
        return result**0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name  
    
class Cluster(object):
    def __init__(self, points, pointType):
        """
        points: list of points
        pointType: subClass of point
        """
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def singleLinkageDist(self, other):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance(p2)
        return minDist
    def maxLinkageDist(self, other):
        maxDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
        return maxDist
    def averageLinkageDist(self, other):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance(p2)
        return totDist/(len(self.points)*len(other.points))
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def members(self):
        for p in self.points:
            yield p
    def isIn(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __repr__(self):
        names = []
        for p in self.points:
            names.append(p.getName())
        names.sort()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]
    def __str__(self):
        names = []
        for p in self.points:
            names.append(p.getName())
        names.sort()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        """compute centroid value
        return a Point('mean', [])
        """
        #print "Compute Centroid for the cluster: ", self
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        #print "construct a new centroid Point"
        centroid = self.pointType(
            'mean',
            totVals/float(len(self.points)),
            totVals/float(len(self.points)))
        return centroid

class ClusterSet(object):
    def __init__(self, pointType):
        self.members = []
    def add(self, c):
        """c is a single cluster"""
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]
    def mergeClusters(self, c1, c2):
        """c1 and c2 are Cluster type"""
        print "***** calling merge Clusters"
        print "mergeClusters c({}) and c({})".format(c1, c2)
        points = []
        for p in c1.members():
            points.append(p)
        for p in c2.members():
            points.append(p)
        newC = Cluster(points, type(p))
        self.members.remove(c1)
        self.members.remove(c2)
        self.add(newC)
        return c1, c2
    def findClosest(self, metric):
        print "***** calling find Closest"
        print ">>>>>>>>>>>>>>>>>>>>>>>there are # self.members: ", len(self.members)
        for i in self.members:
            print "--->", i
        minDistance = metric(self.members[0], self.members[1])
        toMerge = (self.members[0], self.members[1])
        for c1 in self.members:
            for c2 in self.members:
                if c1 == c2:
                    continue
                if metric(c1, c2) < minDistance:
                    minDistance = metric(c1, c2)
                    toMerge = (c1, c2)
        return toMerge    
    def mergeOne(self, metric, toPrint = False):
        print "***** calling mergeOne*****"
        if len(self.members) == 1:
            print "only one member"
            return None
        if len(self.members) == 2:
            print "only TWO members"
            return self.mergeClusters(self.members[0],
                                      self.members[1])
        toMerge = self.findClosest(metric)
        if toPrint:
            print 'Merged'
            print '  ' + str(toMerge[0])
            print 'with'
            print '  ' + str(toMerge[1])
        self.mergeClusters(toMerge[0], toMerge[1])
        return toMerge
    def mergeN(self, metric, numClusters = 1, history = [],
               toPrint = False):
        print "############################################## calling merge N !!!"
        assert numClusters >= 1
        while len(self.members) > numClusters:
            merged = self.mergeOne(metric, toPrint)
            history.append(merged)
        return history
    def numClusters(self):
        return len(self.members) + 1
    def __str__(self):
        result = ''
        for c in self.members:
            result = result + str(c) + '\n'
        return result
    def __repr__(self):
        result = ''
        for c in self.members:
            result = result + str(c) + '\n'
        return result

#US Counties example
class County(Point):
    #Interesting subsets of features
    #0=don't use, 1=use
    noWealth = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '0'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    wealthOnly = (('HomeVal', '1'), ('Income', '1'), ('Poverty', '1'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '0'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '1'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    education = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '0'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '0'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    noEducation = (('HomeVal', '1'), ('Income', '0'), ('Poverty', '1'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    gender = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    allFeatures = (('HomeVal', '1'), ('Income', '0'), ('Poverty', '1'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '1'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    filterNames = {'all': allFeatures, 'education': education,
                   'noEducation': noEducation,
                   'wealthOnly': wealthOnly,'noWealth': noWealth, 'gender': gender}
    attrFilter = None
    #Override Point to construct subset of features
    def __init__(self, name, originalAttrs, normalizedAttrs = None,
                 filterName = 'all'):
        """County.attrFiler is None means it is the first time
        we have generated a point of type County
        Then we set up the filter to look at attr of value 1
        """
        if County.attrFilter == None:
            County.attrFilter = ''
            filterSpec = County.filterNames[filterName]
            for f in filterSpec:
                County.attrFilter += f[1] # a string
        Point.__init__(self, name, originalAttrs, normalizedAttrs)
        features = []
        for i in range(len(County.attrFilter)):
            if County.attrFilter[i] == '1':
                features.append((self.getAttrs()[i]))
        self.features = features
    #Override Point.distance to use only subset of features
    def distance(self, other):
        """instead of all the dimentionality, only the features"""
        result = 0.0
        for i in range(len(self.features)):
            result += (self.features[i] - other.features[i])**2
        return result**0.5

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
            continue
        dataList.append(features)
        nameList.append(name)
    return nameList, dataList, maxVals
    
def buildCountyPoints(fName, filterName = 'all', scale = True):
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        if scale:
            # if scale, normalize by dividing the maxVals array
            normalizedAttrs = originalAttrs/pylab.array(maxVals)
        else:
            normalizedAttrs = originalAttrs
        points.append(County(nameList[i], originalAttrs,
                             normalizedAttrs, filterName))
    return points

def getAveIncome(cluster):
    tot = 0.0
    numElems = 0
    for c in cluster.members():
        tot += c.getOriginalAttrs()[1]
        numElems += 1
    if numElems > 0:
        return tot/numElems
    return 0.0

def test(k = 50, cutoff = 0.01, numTrials = 1, myHome = 'MAMiddlesex',
         filterName = 'all', printPoints = False,
         printClusters = True):
    #Build the set of points
    points = buildCountyPoints('counties.txt', filterName)
    if printPoints:
        print 'Points'
        for p in points:
            attrs = p.getAttrs()
            for i in range(len(attrs)):
                attrs[i] = round(attrs[i], 2)
            print '  ', p, attrs
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
        if printClusters:
            print 'Clusters:'
        for i in range(len(clusters)):
            if printClusters:
                print '  C' + str(i) + ':', clusters[i]
    for c in bestClustering:
        incomes = []
        for i in range(len(bestClustering)):
            incomes.append(getAveIncome(bestClustering[i]))
            if printClusters:
                print '  C' + str(i) + ':', bestClustering[i]
        pylab.hist(incomes)
        pylab.xlim([0,35000])
        pylab.xlabel('Ave. Income')
        pylab.ylabel('Number of Clusters')
        if c.isIn(myHome):
            print '\nHome Cluster:', c
            print 'Ave. income of Home Cluster = ', round(getAveIncome(c),0)

def choseRandom(k = 50, cutoff = 0.01, numTrials = 1, myHome = 'MAMiddlesex',
         filterName = 'all', printClusters = True):
    #Build the set of points
    points = buildCountyPoints('counties.txt', filterName)
    #Choose clusters at random
    random.shuffle(points)
    #print "@@@@@ now shuffled points are: ", points
    print "len points is: ", len(points)
    clusters = []
    size = len(points) / k
    print "size is: ", size
    for j in range(0, len(points), size):
        clusters.append(Cluster(points[j:(j+size)], County))
    print "# of clusters: ", len(clusters)
    if printClusters:
        print 'Clusters:'
    for i in range(len(clusters)):
        if printClusters:
            print '  C' + str(i) + ':', clusters[i]
    for c in clusters:
        incomes = []
        for i in range(len(clusters)):
            incomes.append(getAveIncome(clusters[i]))
            if printClusters:
                print '  C' + str(i) + ':', clusters[i]
        pylab.hist(incomes)
        pylab.xlim([0,35000])
        pylab.xlabel('Ave. Income')
        pylab.ylabel('Number of Clusters')
        if c.isIn(myHome):
            print '\nHome Cluster:', c
            print 'Ave. income of Home Cluster = ', round(getAveIncome(c),0)

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

#Use hierarchical clustering for counties
#It will run for a VERY long time
def test3(fileName, scale = False, filterName = 'all',
          printSteps = False, printHistory = False):
    points = buildCountyPoints(fileName, filterName = filterName,
                               scale = scale)
    cS = ClusterSet(County)
    for p in points:
        cS.add(Cluster([p], County))
    history = cS.mergeN(Cluster.maxLinkageDist, 2, toPrint = printSteps)
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
    print ''
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

if __name__ == "__main__":
    #print 'Cluster on education level only'        
    #test(k = 100, filterName = 'education', numTrials = 2, printClusters = False)
    #pylab.title('Education Level')  
    ##pylab.figure()
    print 'Cluster on gender only'
    test(k = 100, filterName = 'gender', numTrials = 1, printClusters = False)
    pylab.title('Gender')
    pylab.show()

    print 'Choose clusters at random'
    choseRandom(k = 100, numTrials = 2, printClusters = False)
    pylab.title('Random k clusters')  
    ##pylab.figure()
    ##print 'Cluster on gender only'
    ##test(k = 20, filterName = 'gender', numTrials = 1, printClusters = False)
    ##pylab.title('Gender')
    pylab.show()

    ##test(k = 5, filterName = 'all', printClusters = False)
    ##pylab.title('All Features')
    ##pylab.figure()
    ##test(k = 5, filterName = 'wealthOnly', printClusters = False)
    ##pylab.title('Home Value, Income, Unemployed')
    ##pylab.figure()
    ##test(k = 50, filterName = 'education', numTrials = 5, printClusters = False)
    ##pylab.title('Education Level')
    ##pylab.show()
    ##test(k = 50, filterName = 'all', numTrials = 2, printClusters = False)
    ##pylab.title('All Features')
    ##pylab.figure()
    ##test(k = 50, filterName = 'noEducation', numTrials = 2, printClusters = False)
    ##pylab.title('All - Education')
    ##pylab.show()

    #test3('newEngland.txt')
    #test3('newEngland.txt', scale=True)