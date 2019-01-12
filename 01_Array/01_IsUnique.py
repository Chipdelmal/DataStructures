##############################################################################
# 01: Is Unique? Exercise
##############################################################################

def isUnique_Set(inputString):
    '''
    Returns true, if all the characters in the input string are unique.
    This function uses an additional structure (set) to store the unique
        characters already used.
    '''
    lettersSet = {inputString[0]}
    allUnique = True
    for i in range(1, len(inputString)):
        letter = inputString[i]
        if(letter not in lettersSet):
            lettersSet.add(letter)
        else:
            allUnique = False
            break
    return(allUnique)


def isUnique_NoStructs(inputString):
    '''
    Returns true, if all the characters in the input string are unique.
    This function does not use any additional structures. It goes through
        the string element by element, checking for matches.
    '''
    allUnique = True
    for i in range(0, len(inputString)):
        for j in range(i + 1, len(inputString)):
            if inputString[i] == inputString[j]:
                allUnique = False
                break
        if (allUnique is False):
            break
    return(allUnique)


inputString = "abcdbexyz"
uniqueA = isUnique_Set(inputString)
uniqueB = isUnique_NoStructs(inputString)

print([uniqueA, uniqueB])
