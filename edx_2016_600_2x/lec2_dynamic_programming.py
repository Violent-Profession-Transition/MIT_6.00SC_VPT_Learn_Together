def FastFib(n, memo={0:1, 1:1}):
    """memo stores a result based on (n)"""
    print("trying on n: ", n)
    try:
        result = memo[n]
        print("*****inside memo")
        return result
    except:
        print("memo of {} didnot exsits!".format(n))
        result = FastFib(n-1, memo) + FastFib(n-2, memo)
        memo[n] = result
        return result


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

    def __repr__(self):
        return "{}: <{},{}>".format(self.name, self.value, self.calories)

import random

def buildLargeMenu(numItems, maxVal, maxWeight):
    """build large menus of food for knapsack problem"""
    items = []
    for i in range(numItems):
        items.append(
            Food(
                str(i),
                random.randint(1, maxVal),
                random.randint(1, maxWeight)
            )
        )
    return items

def maxVal(remaining_items, remaining_weight):
    """Assumes
    remaining_items: a list of items,
    remaining_weight: a weight,
    Returns a tuple of the total value of a solution
    to 0/1 knapsack problem and
    the items of that solution
    ***the key is maxVal() for withVal and withoutVal is almost identical!
    ***except the remaining_weight is adjusted with withVal
    """
    print("##### New Stack ####")
    print("##### For {} R{} #####".format(remaining_items, remaining_weight))
    total_values = 0
    knapsack_items = ()
    if remaining_items == [] or remaining_weight == 0:
        print("Base case: return (0, ())")
        result = (total_values, knapsack_items)
    elif remaining_items[0].getCost() > remaining_weight:
        # Explore right branch only
        print("Discard left branch, only on Right branch since remaining_items 1st item too heavy...")
        result = maxVal(remaining_items[1:], remaining_weight)
    else:
        nextItem = remaining_items[0]
        # First Explore left branch
        print("First, test left branch>>>")
        withVal, withToTake = maxVal(
            remaining_items[1:],
            remaining_weight - nextItem.getCost()
        )
        print("withVal, withToTake are: ", withVal, withToTake)
        withVal += nextItem.getValue()
        print("Add 1st Left to withVal, ", withVal)
        # Then Explore right branch
        print("Second, test right branch<<<")
        withoutVal, withoutToTake = maxVal(
            remaining_items[1:],
            remaining_weight
        )
        print("withoutVal, withoutToTake are: ", withoutVal, withoutToTake)
        # Explore better branch
        if withVal > withoutVal:
            print("withVal better, add 1st Left item to withToTake in knapsack")
            result = (withVal, withToTake + (nextItem,))
        else:
            print("withoutVal better")
            result = (withoutVal, withoutToTake)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@RESULT For {} R{}, is: {} #####".format(remaining_items, remaining_weight, result))
    return result

def dynamicMaxVal(remaining_items, remaining_weight, memo={}):
    """use dynamic programming to create a memoriztion
    memo is a dict with key of a tuple
    tuple is (remaining_items, remaining_weight)"""
    print("##### New Stack ####")
    print("##### For {} R{} #####".format(remaining_items, remaining_weight))
    try:
        """ first check if the optimal choice of items,
        given the remaining_weight is already in the memo"""
        result = memo[(len(remaining_items), remaining_weight)]
        print("inside memo")
        return result
    except:
        print("memo of {} {} didnot exsits!".format(len(remaining_items), remaining_weight))
        if remaining_items == [] or remaining_weight == 0:
            print("Base case: return (0, ())")
            result = (0, ())
        elif remaining_items[0].getCost() > remaining_weight:
            # Explore right branch only
            print("Discard left branch, only on Right branch since remaining_items 1st item too heavy...")
            result = dynamicMaxVal(remaining_items[1:], remaining_weight, memo)
        else:
            print("go down LEFT branch")
            nextItem = remaining_items[0]
            print("nextItem is: ", nextItem)
            # Explore left branch
            print("First, test left branch>>>")
            withVal, withToTake = dynamicMaxVal(
                remaining_items[1:],
                remaining_weight - nextItem.getCost(),
                memo
            )
            print("withVal, withToTake are: ", withVal, withToTake)
            withVal += nextItem.getValue()
            print("Add 1st Left to withVal, ", withVal)
            # Explore right branch
            print("Second, test right branch<<<")
            withoutVal, withoutToTake = dynamicMaxVal(
                remaining_items[1:],
                remaining_weight,
                memo
            )
            print("withoutVal, withoutToTake are: ", withoutVal, withoutToTake)
            # Explore better branch
            if withVal > withoutVal:
                print("withVal better, add 1st Left to withToTake")
                result = (withVal, withToTake + (nextItem,))
            else:
                print("withoutVal better")
                result = (withoutVal, withoutToTake)
        # last thing, update the memo
        memo[(len(remaining_items), remaining_weight)] = result
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@RESULT For {} R{}, is: {} #####".format(remaining_items, remaining_weight, result))
        return result

def powerSet(items):
    """using bitwise operators (<<, >>, &, |, ~, ^)."""
    N = len(items)
    print("N is: ", N)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print("Now i is: ", i, bin(i))
        combo = []
        for j in range(N):
            print("---Now J is: ", j)
            # test bit jth of integer i
            print("test bit jth of integer i, i>>j: ", i>>j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

gen = powerSet(['a','b','c','d','e'])

def testMaxval(foods, maxWeight, algorithm):
    print("use search tree to allocate ", maxWeight, " weight for ", foods)
    total_values, knapsack_items = algorithm(foods, maxWeight)
    # for item in taken:
    #     print("    ", item)

numItems = 20
items = buildLargeMenu(numItems, 90, 250)
# items = [Food("a",6,3), Food("b",7,2), Food("c",8,3)]
# print("Items by buildLargeMenus is: ", items, numItems)
testMaxval(items, 750, dynamicMaxVal)
# testMaxval(items, 750, maxVal)
