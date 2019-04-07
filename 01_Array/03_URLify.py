##############################################################################
# 03: URLify
##############################################################################


def urlify_Obvious(inString):
    return inString.replace(" ", "%20")


testString = "Testing this solution"
urlify_Obvious(testString)

inString = testString

replaceString = "%20"
stringLength = len(inString)
spacesCount = inString.count(" ")
urlArray = [None] * (3 * spacesCount + stringLength)
arrayIndex = stringLength
for i in range(0, stringLength-1):
    character = inString[i]
    if character is not " ":
        urlArray[arrayIndex] = character
        arrayIndex = arrayIndex - 1
    else:
        for j in range(0, len(replaceString)):
            urlArray[arrayIndex] = replaceString[j]
            arrayIndex = arrayIndex - 1
urlArray
range(stringLength, 1, )
