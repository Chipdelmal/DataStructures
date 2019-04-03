##############################################################################
# 03: URLify
#   Extensions:
##############################################################################


def urlify(inputString, spaceReplacement="%20"):
    '''
    Returns the string with the spaces replaced by the "spaceReplacement"
        parameter. This solution uses an additional structure (not in place).
    '''
    replaceLength = len(spaceReplacement)
    inputLength = len(inputString)
    spacesCount = inputString.count(" ")

    tempArray = [None] * (inputLength + (replaceLength - 1) * spacesCount)

    j = 0
    for i, char in enumerate(inputString):
        if char is " ":
            for replace in spaceReplacement:
                tempArray[j] = replace
                j = j + 1
        else:
            tempArray[j] = char
            j = j + 1
    return tempArray


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    urlified = urlify("This is not a test", spaceReplacement="%20")
