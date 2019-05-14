class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result
    def __repr__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

# test dToB
print "decimal 100 to Binary: ", dToB(100, 7)

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    print("templates are now: ", templates)
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

# test generate Power Set
print "generate Power Set: ", genPset(["Apple", "Cat", "Monkey", "Bull"])

def chooseBest(pset, constraint, getVal, getWeight):
    """
    choose the best value from all the subsets of powerset
    """
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

def testBest():
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

# try brute force with generate all powerset
testBest()