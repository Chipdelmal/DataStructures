##############################################################################
# 02: Check Permutation
#   Extensions: Case insensitive, spaces
##############################################################################


def caseAndSpaceTreat(inputString, caseSensitive=True, spaces=True):
    '''
    Returns a lowercase string if case insensitive, and removes spaces
        if necessary
    '''
    # String pre-treatment
    if caseSensitive == False:
        inputString = inputString.lower()
    if spaces == False:
        inputString = inputString.replace(" ", "")
    return inputString

def permutation_Sort(inStringA, inStringB, caseSensitive=True, spaces=True):
    '''
    Returns true if the two strings are permutations of one another.
    This function works by sorting the two strings, and then comparing them
        to check if the resulting structure is the same.
    '''
    inStringA = caseAndSpaceTreat(inStringA,caseSensitive,spaces)
    inStringB = caseAndSpaceTreat(inStringB,caseSensitive,spaces)
    sortedA = sorted(inStringA)
    sortedB = sorted(inStringB)
    return (sortedA == sortedB)


def countCharacters(inString):
    '''
    Returns a dictionary with the count of characters in the provided string.
    '''
    tempDict = {}
    for char in set(inString):
        tempDict[char] = inString.count(char)
    return(tempDict)


def permutation_Count(inStringA, inStringB, caseSensitive=True, spaces=True):
    '''
    Returns true if the two strings are permutations of one another.
    This function generates an additional set per string to count the times
        a character repeats itself in each of them (uses an auxiliary
        "countCharacters" function).
    '''
    inStringA = caseAndSpaceTreat(inStringA,caseSensitive,spaces)
    inStringB = caseAndSpaceTreat(inStringB,caseSensitive,spaces)
    countA = countCharacters(inStringA)
    countB = countCharacters(inStringB)
    return (countA == countB)


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    case = True
    spaces = True
    inStringA = "test "
    inStringB = "etst"
    permutation_Sort(inStringA, inStringB, caseSensitive=case, spaces=spaces)
    permutation_Count(inStringA, inStringB, caseSensitive=case, spaces=spaces)
