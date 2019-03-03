word_list = ["tab", "bat", "go", "dota", "python", "bear", "singapore"]
def findAll(wordList, lStr):
    """
    assumes: wordList is a list of words in lowercase.
             lStr is a str of lowercase letters.
             No letter occurs in lStr more than once
    returns: a list of all the words in wordList that contain
             each of the letters in lStr exactly once and no
             letters not in lStr.
    """
    result = []
    for word in wordList:
        for letter in word:
            if letter not in list(lStr):
                break
        else:
            result.append(word) # only if inner loop did NOT break

    return result

assert(findAll(word_list, "listen") == [])
assert(findAll(word_list, "og") == ["go"])
assert(findAll(word_list, "arbe") == ["bear"])
assert(findAll(word_list, "abt") == ["tab", "bat"])

def addVectors(v1, v2):
    """
     assumes v1 and v2 are lists of ints.
     Returns a list containing the pointwise sum of
     the elements in v1 and v2. For example,
     addVectors([4,5], [1,2,3]) returns [5,7,3],and
     addVectors([], []) returns []. Does not modify inputs.
    """
    v1_copy, v2_copy = v1[:], v2[:]
    if len(v1) < len(v2):
        longer_vector = v2_copy
        shorter_vector = v1_copy
    else:
        longer_vector = v1_copy
        shorter_vector = v2_copy
    for i in range(len(shorter_vector)):
        longer_vector[i] += shorter_vector[i]
    return longer_vector


    #  result = []
    #  shared_length = len(v1) if len(v1) < len(v2) else len(v2)
    #  for i in range(shared_length):
        #  result.append(v1[i] + v2[i])
    #  if len(v1) < len(v2):
        #  result += v2[shared_length:]
    #  else:
        #  result += v1[shared_length:]
    #  return result


assert(addVectors([4,5], [1,2,3]) == [5,7,3])
assert(addVectors([], []) == [])
input1 = [1,3,5]
input2 = [9]
assert(addVectors(input1, input2) == [10,3,5])
assert(input1 == [1,3,5])