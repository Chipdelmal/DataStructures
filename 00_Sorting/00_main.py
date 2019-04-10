# https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
    return list


def bubbleSort(list):
    n, swapped, x = (len(list), True, -1)
    while swapped:
        swapped, x = (False, x + 1)
        for i in range(1, n-x):
            if list[i - 1] > list[i]:
                list = swap(list, i - 1, i)
                swapped = True
    return list


def selectionSort(list):
    n = len(list)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j
        list = swap(list, i, min)
    return list


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    testList = [1, 3, 5, 2, 1, 7, 6]
    bubbleSort(testList)
    selectionSort(testList)
