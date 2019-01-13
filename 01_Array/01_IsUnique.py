##############################################################################
# 01: Is Unique?
#   Extensions: Case insensitive, spaces
##############################################################################


def isUnique_Set(inputString, caseSensitive=True, spaces=True):
    '''
    Returns true, if all the characters in the input string are unique.
    This function uses an additional structure (set) to store the unique
        characters already used.
    '''
    # String pre-treatment
    if caseSensitive == False:
        inputString = inputString.lower()
    if spaces == False:
        inputString = inputString.replace(" ", "")
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
    if caseSensitive == False:
        inputString = inputString.lower()
    if spaces == False:
        inputString = inputString.replace(" ", "")
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
    inputString = "abc dez xy"
    case = False
    spaces = True
    uniqueA = isUnique_Set(inputString,caseSensitive=case, spaces=spaces)
    uniqueB = isUnique_NoStructs(inputString,caseSensitive=case, spaces=spaces)
    print(
        "Sets: " + str(uniqueA) + "\n"
        + "NoStruct: " + str(uniqueB) + "\n"
        + "\n"
        "Match: " + str(uniqueA == uniqueB)
    )
