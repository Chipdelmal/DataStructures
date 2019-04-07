##############################################################################
# 01: Is Unique?
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

def isUnique_Set(inputString, caseSensitive=True, spaces=True):
    '''
    Returns true, if all the characters in the input string are unique.
    This function uses an additional structure (set) to store the unique
        characters already used.
    '''
    inputString = caseAndSpaceTreat(inputString,caseSensitive,spaces)
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


def isUnique_NoStructs(inputString, caseSensitive=True, spaces=True):
    '''
    Returns true, if all the characters in the input string are unique.
    This function does not use any additional structures. It goes through
        the string element by element, checking for matches.
    '''
    inputString = caseAndSpaceTreat(inputString,caseSensitive,spaces)
    allUnique = True
    for i in range(0, len(inputString)):
        for j in range(i + 1, len(inputString)):
            if inputString[i] == inputString[j]:
                allUnique = False
                break
        if (allUnique is False):
            break
    return(allUnique)


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    inputString = "aAbcdez xy"
    case = True
    spaces = False
    uniqueA = isUnique_Set(inputString, caseSensitive=case, spaces=spaces)
    uniqueB = isUnique_NoStructs(inputString, caseSensitive=case, spaces=spaces)
    print(
        "Sets: " + str(uniqueA) + "\n"
        + "NoStruct: " + str(uniqueB) + "\n"
        + "\n"
        "Match: " + str(uniqueA == uniqueB)
    )
