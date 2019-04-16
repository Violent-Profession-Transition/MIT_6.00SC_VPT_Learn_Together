class Food:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.calories = weight

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return "{}: <{},{}>".format(self.name, self.value, self.calories)

def buildMenu(names, values, calories):
    """return a list of foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """assumes items a list, maxCost >=0,
    keyFunction maps elements of items to numbers"""
    # keyFunction makes the function flexible
    # keyFunction will determine how we sort the items
    # sorted returns a list
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return result, totalValue

def testGreedy(items, constraint, keyFunction):
    """test the result from Greedy"""
    taken, value = greedy(items, constraint, keyFunction)
    print("Total value of items taken = ", value)
    for item in taken:
        print("\t", item)

def testGreedys(foods, maxUnits):
    """calls greedy over and over again"""
    print("Use greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)

    print("\nUse greedy by cost to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

    print("\nUse greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
for f in foods:
    print(f)
testGreedys(foods, 750)
testGreedys(foods, 100)
testGreedys(foods, 1000)
