##############################################################################
# 04: Palindrome Permutation
#   Extensions:
##############################################################################


def countOdds(frequenciesList):
    '''
    Returns the number of odd counts in a list of frequencies.
    '''
    oddCount = 0
    for val in frequenciesList:
        if val % 2 != 0:
            oddCount = oddCount + 1
    return oddCount


def characterCounts(inputString):
    '''
    Returns a dictionary with the characters frequencies in a string.
    '''
    dict = {}
    for char in set(inputString):
        dict[char] = inputString.count(char)
    return dict


def treatString(inputString):
    '''
    Returns a string ready to be tested for palindrome
    '''
    removedSpace = inputString.replace(" ", "")
    lowerCase = removedSpace.lower()
    return lowerCase


def naiveIsPalindromePermutation(inputString):
    '''
    Checks if the input string is a permutation of a palindrome.
        This is inefficient as it has to go through the whole array before
        returing the result.
    '''
    treatedString = treatString(inputString)
    frequencies = characterCounts(treatedString).values()
    oddCount = countOdds(frequencies)

    isPalindrome = False
    if len(treatedString) % 2 == 0:
        if oddCount == 0:
            isPalindrome = True
    else:
        if oddCount == 1:
            isPalindrome = True

    return isPalindrome








##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    inputString = "Taco cat"
    print(naiveIsPalindromePermutation(inputString))
