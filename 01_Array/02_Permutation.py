##############################################################################
# 02: Check Permutation
#   Extensions: Case insensitive, spaces
##############################################################################


def permutation_Sort(inStringA, inStringB):
    sortedA = sorted(inStringA)
    sortedB = sorted(inStringB)
    return (sortedA == sortedB)


def countCharacters(inString):
    tempDict = {}
    for char in set(inString):
        tempDict[char] = inString.count(char)
    return(tempDict)


def permutation_Count(inStringA, inStringB):
    countA = countCharacters(inStringA)
    countB = countCharacters(inStringB)
    return (countA == countB)


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    inStringA = "test"
    inStringB = "etst"
    permutation_Sort(inStringA, inStringB)
    permutation_Count(inStringA, inStringB)
