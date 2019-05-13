import ps9

VALUE = 0
WORK = 1
def test_loadSubjects():
    expected = {'6.08': (1, 10), '6.09': (3, 7), '6.19': (8, 19), '6.10': (8, 18), '6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.03': (2, 9), '6.04': (1, 2), '6.05': (1, 18), '6.06': (5, 19), '6.07': (2, 10), '6.13': (9, 16), '6.18': (10, 4), '6.15': (10, 6), '6.16': (6, 9), '6.12': (6, 3), '6.17': (9, 3), '6.14': (10, 8), '6.11': (6, 8)}
    actual = {}
    failed = False
    try:
        actual = ps9.loadSubjects("shortened_subjects.txt")
    except Exception,e:
        failed = True
        print("ERROR in loadSubjects: Error while loading subjects:", e.value)
    try:
        test600 = actual['6.00']
    except:
        print("ERROR in loadSubjects: loadSubjects did not return '6.00' as a key")
        failed = True
    if test600 != (10, 1):
        print("ERROR in loadSubjects: Expected 6.00 to have value (10, 1), but was actually " + str(test600))
        failed = True
    if expected != actual:
        print("ERROR in loadSubjects: Expected " + str(expected) + " but was actually " + str(actual))
        failed = True
    if failed:
        raise Exception

def test_cmpValue():
    subInfo1 = (3, 4)
    subInfo2 = (3, 5)
    subInfo3 = (2, 7)
    subInfo4 = (2, 2)

    failed = False

    shouldBeFalse = ps9.cmpValue(subInfo1, subInfo2)
    if type(shouldBeFalse) != bool:
        failed = True
        print("ERROR in cmpValue: return value should be boolean but was actually " + str(type(shouldBeFalse)))
    if shouldBeFalse == True:
        failed = True
        print("ERROR in cmpValue: cmpValue((3, 4), (3, 5)) should be False but was actually " + str(shouldBeFalse))
    shouldBeTrue = ps9.cmpValue(subInfo1, subInfo3)
    if type(shouldBeTrue) != bool:
        failed = True
        print("ERROR in cmpValue: return value should be boolean but was actually " + str(type(shouldBeTrue)))
    if shouldBeTrue == False:
        failed = True
        print("ERROR in cmpValue: cmpValue((3, 4), (2, 7)) should be True but was actually " + str(shouldBeTrue))
    shouldBeTrue = ps9.cmpValue(subInfo1, subInfo4)
    if type(shouldBeTrue) != bool:
        failed = True
        print("ERROR in cmpValue: return value should be boolean but was actually " + str(type(shouldBeTrue)))
    if shouldBeTrue == False:
        failed = True
        print("ERROR in cmpValue: cmpValue((3, 4), (2, 2)) should be True but was actually " + str(shouldBeTrue))
    if failed:
        raise Exception

def test_cmpWork():
    subInfo1 = (4, 3)
    subInfo2 = (5, 3)
    subInfo3 = (7, 2)
    subInfo4 = (2, 2)

    failed = False

    shouldBeFalse = ps9.cmpWork(subInfo1, subInfo2)
    if type(shouldBeFalse) != bool:
        failed = True
        print("ERROR in cmpWork: return value should be boolean but was actually " + str(type(shouldBeFalse)))
    if shouldBeFalse == True:
        failed = True
        print("ERROR in cmpWork: cmpWork((4, 3), (5, 3)) should be False but was actually " + str(shouldBeFalse))
    shouldBeFalse = ps9.cmpWork(subInfo1, subInfo3)
    if type(shouldBeFalse) != bool:
        failed = True
        print("ERROR in cmpWork: return value should be boolean but was actually " + str(type(shouldBeFalse)))
    if shouldBeFalse == True:
        failed = True
        print("ERROR in cmpWork: cmpWork((4, 3), (7, 2)) should be False but was actually " + str(shouldBeFalse))
    shouldBeTrue = ps9.cmpWork(subInfo4, subInfo1)
    if type(shouldBeTrue) != bool:
        failed = True
        print("ERROR in cmpWork: return value should be boolean but was actually " + str(type(shouldBeTrue)))
    if shouldBeTrue == False:
        failed = True
        print("ERROR in cmpWork: cmpWork((4, 3), (2, 2)) should be True but was actually " + str(shouldBeTrue))
    if failed:
        raise Exception
        

def test_cmpRatio():
    # Test to make sure they're converting to floats
    subInfo1 = (1, 5)
    subInfo2 = (2, 4)

    failed = False

    shouldBeTrue = ps9.cmpRatio(subInfo2, subInfo1)
    if type(shouldBeTrue) != bool:
        failed = True
        print("ERROR in cmpRatio: return value should be boolean but was actually " + str(type(shouldBeTrue)))
    if shouldBeTrue == False:
        failed = True
        print("ERROR in cmpRatio: cmpRatio((2, 4), (1, 5)) should be True but was actually " + str(shouldBeTrue))

    # Test when they're equal
    subInfo1 = (4, 8)
    subInfo2 = (2, 4)

    shouldBeFalse = ps9.cmpRatio(subInfo1, subInfo2)
    if type(shouldBeFalse) != bool:
        failed = True
        print("ERROR in cmpRatio: return value should be boolean but was actually " + str(type(shouldBeFalse)))        
    if shouldBeFalse == True:
        failed = True
        print("ERROR in cmpRatio: cmpRatio((4, 8), (2, 4)) should be False but was actually " + str(shouldBeFalse))
    if failed:
        raise Exception

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2
        
def cmpSum(subInfo1, subInfo2):
    assert type(subInfo1) == tuple, "Arguments to comparator should be tuples"
    assert type(subInfo2) == tuple, "Arguments to comparator should be tuples"
    return sum(subInfo1) > sum(subInfo2)

def test_greedyAdvisor():
    subjects = {}
    subjects['6.00'] = (10, 1)
    subjects['6.01'] = (8, 4)
    subjects['6.02'] = (5, 8)
    subjects['6.03'] = (1, 1)
    subjects['6.04'] = (5, 15)
    newsubjects = subjects.copy()
    dontmutate = subjects.copy()
    expected = {}
    expected['6.04'] = (5, 15)
    expected['6.00'] = (10, 1)
    expected['6.03'] = (1, 1)

    failed = False
    print
    print "subjects = " + str(subjects)
    print "Trying greedyAdvisor(subjects, 17, cmpSum)..."
    try:
        actual = ps9.greedyAdvisor(subjects, 17, cmpSum)
    except Exception,e:
        failed = True
        print("ERROR in greedyAdvisor (probably does not handle a new comparator) " + str(e))
    else:
        if expected != actual:
            failed = True
            print("ERROR in greedyAdvisor: For greedyAdvisor(subjects, 17, cmpSum), expected " + str(expected) + " but was actually " + str(actual))
    if dontmutate != subjects:
        failed = True
        print("ERROR in greedyAdvisor: subjects was mutated")


    expected = {}
    expected['6.02'] = (5, 8)
    subjects = newsubjects.copy()
    print "Trying greedyAdvisor(subjects, 8, cmpSum)..."
    try:
        actual = ps9.greedyAdvisor(subjects, 8, cmpSum)
    except Exception,e:
        failed = True
        print("ERROR in greedyAdvisor (probably does not handle a new comparator) " + str(e))
    else:
        if expected != actual:
            failed = True
            print("ERROR in greedyAdvisor: For greedyAdvisor(subjects, 8, cmpSum), expected " + str(expected) + " but was actually " + str(actual))  

    # Small Catalog handout tests
    print
    smallCatalog = {'6.00': (16, 8), '1.00': (7, 7), '15.01': (9, 6), '6.01': (5, 3)}
    print "smallCatalog = " + str(smallCatalog)
    print "Trying greedyAdvisor(smallCatalog, 15, cmpValue)..."
    expected = {'6.00': (16, 8), '15.01': (9, 6)}
    actual = ps9.greedyAdvisor(smallCatalog.copy(), 15, cmpValue)
    if expected != actual:
        failed = True
        print("ERROR in greedyAdvisor: For greedyAdvisor(smallCatalog, 15, ps9.cmpValue), expected " + str(expected) + " but was actually " + str(actual))
    expected = {'6.01': (5, 3), '15.01': (9, 6)}
    print "Trying greedyAdvisor(smallCatalog, 15, cmpWork)..."
    actual = ps9.greedyAdvisor(smallCatalog.copy(), 15, cmpWork)
    if expected != actual:
        failed = True
        print("ERROR in greedyAdvisor: For greedyAdvisor(smallCatalog, 15, ps9.cmpWork), expected " + str(expected) + " but was actually " + str(actual))
    expected = {'6.00': (16, 8), '6.01': (5, 3)}
    print "Trying greedyAdvisor(smallCatalog, 15, cmpRatio)..."
    actual = ps9.greedyAdvisor(smallCatalog.copy(), 15, cmpRatio)
    if expected != actual:
        failed = True
        print("ERROR in greedyAdvisor: For greedyAdvisor(smallCatalog, 15, ps9.cmpRatio), expected " + str(expected) + " but was actually " + str(actual))
    if failed:
        raise Exception

def sumValues(d):
    s = 0
    for val in d.values():
        s += val[VALUE]
    return s

def test_bruteForceAdvisor():
    #shortenedSubjects = {'6.08': (1, 10), '6.09': (3, 7), '6.19': (8, 19), '6.10': (8, 18), '6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.03': (2, 9), '6.04': (1, 2), '6.05': (1, 18), '6.06': (5, 19), '6.07': (2, 10), '6.13': (9, 16), '6.18': (10, 4), '6.15': (10, 6), '6.16': (6, 9), '6.12': (6, 3), '6.17': (9, 3), '6.14': (10, 8), '6.11': (6, 8)}
    shortenedSubjects = {'6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.04': (1, 2), '6.18': (10, 4), '6.15': (10, 6), '6.12': (6, 3), '6.17': (9, 3)}
    dontmutate = shortenedSubjects.copy()

    failed = False
    expected = {'6.00': (10, 1), '6.04': (1, 2)}
    print
    print "shortenedSubjects = " + str(shortenedSubjects)
    print "Trying bruteForceAdvisor(shortenedSubjects, 3)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 3)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 3), expected " + str(expected) + " but was actually " + str(actual))
    if dontmutate != shortenedSubjects:
        failed = True
        print("ERROR in bruteForceAdvisor: subjects was mutated")
    shortenedSubjects = {'6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.04': (1, 2), '6.18': (10, 4), '6.15': (10, 6), '6.12': (6, 3), '6.17': (9, 3)}
    expected = {'6.00': (10, 1), '6.17': (9, 3)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 4)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 4)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 4), expected " + str(expected) + " but was actually " + str(actual))
    
    shortenedSubjects = {'6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.04': (1, 2), '6.18': (10, 4), '6.15': (10, 6), '6.12': (6, 3), '6.17': (9, 3)}
    expected = {'6.00': (10, 1), '6.18': (10, 4)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 5)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 5)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 5), expected " + str(expected) + " but was actually " + str(actual))
    shortenedSubjects = {'6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.04': (1, 2), '6.18': (10, 4), '6.15': (10, 6), '6.12': (6, 3), '6.17': (9, 3)}
    expected = {'6.00': (10, 1), '6.17': (9, 3)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 6)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 6)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 6), expected " + str(expected) + " but was actually " + str(actual))
    shortenedSubjects = {'6.00': (10, 1), '6.01': (5, 4), '6.02': (5, 6), '6.04': (1, 2), '6.18': (10, 4), '6.15': (10, 6), '6.12': (6, 3), '6.17': (9, 3)}
    expected = {'6.00': (10, 1), '6.12': (6, 3), '6.17': (9, 3)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 7)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 7)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 7), expected " + str(expected) + " but was actually " + str(actual))
    

    shortenedSubjects = {'12.02': (5, 5), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3), '12.06': (2, 5), '12.08': (2, 4), '12.09': (8, 2), '12.15': (10, 7)}
    print
    print "shortenedSubjects = " + str(shortenedSubjects)
    expected = {'12.09': (8, 2), '12.04': (7, 1)}
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 3)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 3), expected " + str(expected) + " but was actually " + str(actual))
    shortenedSubjects = {'12.02': (5, 5), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3), '12.06': (2, 5), '12.08': (2, 4), '12.09': (8, 2), '12.15': (10, 7)}
    expected = {'12.09': (8, 2), '12.03': (2, 1), '12.04': (7, 1)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 4)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 4)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 4), expected " + str(expected) + " but was actually " + str(actual))
    
    shortenedSubjects = {'12.02': (5, 5), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3), '12.06': (2, 5), '12.08': (2, 4), '12.09': (8, 2), '12.15': (10, 7)}
    expected = {'12.09': (8, 2), '12.03': (2, 1), '12.04': (7, 1)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 5)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 5)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 5), expected " + str(expected) + " but was actually " + str(actual))
    shortenedSubjects = {'12.02': (5, 5), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3), '12.06': (2, 5), '12.08': (2, 4), '12.09': (8, 2), '12.15': (10, 7)}
    expected = {'12.09': (8, 2), '12.04': (7, 1), '12.07': (6, 3)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 6)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 6)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 6), expected " + str(expected) + " but was actually " + str(actual))
    shortenedSubjects = {'12.02': (5, 5), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3), '12.06': (2, 5), '12.08': (2, 4), '12.09': (8, 2), '12.15': (10, 7)}
    expected = {'12.09': (8, 2), '12.03': (2, 1), '12.04': (7, 1), '12.07': (6, 3)}
    print "Trying bruteForceAdvisor(shortenedSubjects, 7)..."
    (total_value, actual) = ps9.bruteForceAdvisor(shortenedSubjects, 7)
    if expected != actual and sumValues(expected) > sumValues(actual):
        failed = True
        print("ERROR in bruteForceAdvisor: For bruteForceAdvisor(shortenedSubjects, 7), expected " + str(expected) + " but was actually " + str(actual))
    if failed:
        raise Exception
    

if __name__ == '__main__':
    count = 0
    for function in [test_loadSubjects, test_cmpValue, test_cmpWork, test_cmpRatio, test_greedyAdvisor, test_bruteForceAdvisor]:
        try:
            function()
            print function.func_name, "passed"
            count += 1
        except Exception,e:
            print function.func_name, "failed", e
    print "Passed:", count, "/", 6
