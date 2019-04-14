# https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html


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


def insertionSort(list):
    n = len(list)
    for i in range(n):
        cursor = list[i]
        pos = i
        while (pos > 0) and (list[pos - 1] > cursor):
            list[i] = list[i-1]


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", alist)


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    testList = [1, 3, 5, 2, 1, 7, 6]
    bubbleSort(testList)
    selectionSort(testList)

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)
