# 6.00 Problem Set 9
#
# Intelligent Course Advisor

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
# dictionary mapping subject names to tuples,
# where the tuples are pairs of (learning value, work hours) integers
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    subject_dict = {}
    inputFile = open(filename)
    for line in inputFile:
        subject = line.split(",")
        subject_name = subject[0]
        subject_VW = (int(subject[1]), int(subject[2].strip('\r\n')))
        subject_dict[subject_name] = subject_VW
    return subject_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#

"""
The notion of best is determined by the use
of the comparator
The comparator is a function that takes two argument each of which is a
(value, work) tuple and returns a boolean indicating whether the first argument is better
than the second
"""
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[VALUE] > subInfo2[VALUE]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[WORK] < subInfo2[WORK]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    sub1_VW_ratio = float(subInfo1[VALUE]) / float(subInfo1[WORK])
    sub2_VW_ratio = float(subInfo2[VALUE]) / float(subInfo2[WORK])
    return sub1_VW_ratio > sub2_VW_ratio

def cmpSum(subInfo1, subInfo2):
    assert type(subInfo1) == tuple, "Arguments to comparator should be tuples"
    assert type(subInfo2) == tuple, "Arguments to comparator should be tuples"
    return sum(subInfo1) > sum(subInfo2)

def getValue(subInfo1):
    return subInfo1[1][VALUE]

def getWork(subInfo1):
    return 1.0/subInfo1[1][WORK]

def getVWratio(subInfo1):
    sub1_VW_ratio = float(subInfo1[1][VALUE]) / float(subInfo1[1][WORK])
    return sub1_VW_ratio

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # generate a copy of the subjects dictionary
    subject_dict = subjects.copy()
    # create a list from the subjects
    subject_list = []
    for subject in subject_dict:
        subject_list.append(
            (
                subject, subject_dict[subject]
            )
        )
        # [('6.01', (5, 3)), ...]
    # sort the subject_list according to the comparator
    # reverse = True, give the BEST subject first
    sorted_subject_list = sorted(subject_list, key=comparator, reverse=True)
    print("sorted_subject_list is: ", sorted_subject_list)
    # advised_subjects from the sorted list
    advised_subjects = {}
    totalWork = 0
    for subject in sorted_subject_list:
        print("subject is: ", subject)
        if totalWork + subject[1][WORK] > maxWork:
            break
        else:
            advised_subjects[subject[0]] = subject[1]
            totalWork += subject[1][WORK]
    return advised_subjects

# test Problem 2
# subjects = loadSubjects("shortened_subjects.txt")
# print greedyAdvisor(subjects, 7, getWork)
# print greedyAdvisor(subjects, 7, getValue)
# print greedyAdvisor(subjects, 7, getVWratio)

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    print("##### New Stack ####")
    print("##### For {} R{} #####".format(subjects, maxWork))
    try:
        # generate a copy of the subjects dictionary
        subject_dict = subjects.copy()
        # create a list from the subjects
        subject_list = []
        for subject in subject_dict:
            subject_list.append(
                (
                    subject, subject_dict[subject]
                )
            )
            # [('6.01', (5, 3)), ...]
    except:
        subject_list = subjects[:]
    # maxWork map to remaining_work
    remaining_work = maxWork
    # initial params
    advised_subjects = {}
    """
    Returns a tuple of the total value of a solution
    to 0/1 knapsack problem and
    the items of that solution
    return (max_value, items_for_this_value))
    """
    # base case
    # when subject_list is empty, or when remaining_work is empty
    if subject_list == [] or remaining_work == 0:
        print("Base case: return (0, {})")
        return (0, {})
    # recursive case
    nextItem = subject_list[0]
    if nextItem[1][1] > remaining_work:
        # explore the right branch only
        print("Discard left branch, only on Right branch since remaining_items 1st item too heavy... For {} R{}"
            .format(subjects, remaining_work))
        return bruteForceAdvisor(subject_list[1:], remaining_work)
    else:
        print("First, test with Value branch>>> For {} R{}".format(subjects, remaining_work))
        # with nextItem
        withVal, withToTake = bruteForceAdvisor(
            subject_list[1:], remaining_work - nextItem[1][1]
        )
        print("withVal, withToTake are: ", withVal, withToTake, "For {} R{}"
            .format(subjects, remaining_work))
        withVal += nextItem[1][0]
        print("Add 1st Left to withVal, ", withVal)
        # without nextItem
        print("Second, test withOUT Value branch<<< For {} R{}".format(subjects, remaining_work))
        withoutVal, withoutToTake = bruteForceAdvisor(
            subject_list[1:], remaining_work
        )
        print("withoutVal, withoutToTake are: ", withoutVal, withoutToTake, "For {} R{}"
            .format(subjects, remaining_work))
        # compare
        if withVal > withoutVal:
            # withVal better
            print("withVal better, add 1st Left item to withToTake in knapsack")
            advised_subjects[nextItem[0]] = nextItem[1]
            advised_subjects.update(withToTake)
            result = (withVal, advised_subjects)
            print("@@@RESULT For {} R{}, is: {} #####".format(subjects, remaining_work, result))
            return result
        else:
            # withoutVal better
            print("withoutVal better")
            advised_subjects.update(withoutToTake)
            result = (withoutVal, advised_subjects)
            print("***RESULT For {} R{}, is: {} #####".format(subjects, remaining_work, result))
            return result

# enumerate all the powerset and choose the best
def dToB(num, num_digits):
    """
    return num int in decimal to binary digits
    str with length num_digits, prefilled with '0'
    """
    assert 2**num_digits > num
    bin_Digit = ''
    while num > 0:
        bin_Digit = str(num % 2) + bin_Digit
        num = num // 2
    while len(bin_Digit) < num_digits:
        bin_Digit = "0" + bin_Digit
    return bin_Digit

# test decimal to binary function
print dToB(5, 3)
print dToB(9, 4)
# print dToB(8, 5)
# print dToB(15, 4)

def Pset(items):
    """
    generate the whole power set of items
    items: list
    return list of lists based on the binary digits
    """
    # first generate the binary_digit mapping for powerset
    vector_I = []
    Pset = []
    num_digits = len(items)
    for i in range(2**num_digits):
        vector_I.append(dToB(i, num_digits))
    for num in vector_I:
        print "now trying num in vector_I: ", num
        subset = []
        digits = len(num)
        for j in range(digits):
            if num[j] == "1":
                subset += [items[j]]
                print "subset is now: ", subset
        Pset.append(subset)
    return Pset

# test Pset()
print Pset(["a", "b"])


def Pset_recursive(items):
    """
    recursively generate the powerset
    items: list
    return list of lists of all subsets
    """
    print "new stack with ->", items
    # base case
    if len(items) == 0:
        print "base case, return [[]]"
        return [[]]
    # recursive case
    else:
        nextItem = items[0]
        withToTake = []
        withoutToTake = Pset_recursive(items[1:])
        for item in withoutToTake:
            withToTake.append(item + [nextItem])
        return withToTake + withoutToTake

# test Pset_recursive()
# print Pset_recursive(["a", "b"])

def chooseBestPset(items, maxWeight):
    """
    enumerate all the subsets
    items: a dict
    pick the best value subset that meets the constrainst
    """
    bestValue = 0.0
    bestSubset = []
    subject_list = []
    for subject in items:
        subject_list.append(
            (
                subject, items[subject]
            )
        )
    subsets = Pset_recursive(subject_list)
    for subset in subsets:
        print "now checking subset: ", subset
        totalValue = 0.0
        totalWeight = 0.0
        for item in subset:
            totalValue += item[1][0]
            totalWeight += item[1][1]
        print subset, " has totalValue and totalWeight of", totalValue, totalWeight
        if totalValue > bestValue and totalWeight <= maxWeight:
            bestSubset = subset
            bestValue = totalValue
    return bestSubset

# test Problem 3
subjects = loadSubjects("shortened_subjects.txt")
"""subjects = {
    '6.00': (16, 8),
    '1.00': (7, 7),
    '6.01': (5, 3),
    '15.01': (9, 6)
}"""
#print bruteForceAdvisor(subjects, 3)
#print bruteForceAdvisor(subjects, 4)
#print bruteForceAdvisor(subjects, 5)
#print bruteForceAdvisor(subjects, 7)
# (25, {'6.00': (10, 1), '6.12': (6, 3), '6.17': (9, 3)})
#print chooseBestPset(subjects, 7)
# [('6.17', (9, 3)), ('6.12', (6, 3)), ('6.00', (10, 1))]