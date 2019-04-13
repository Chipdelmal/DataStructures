#!/bin/python3

import math
import os
import random
import re
import sys


# Rotate Left #################################################################
def rotLeft(a, d):
    n = len(a)
    rot = [None] * n
    for i in range(n):
        index = (i - d) % n
        rot[index] = a[i]
    return rot


# Sock Pairs ##################################################################
def sockMerchant(n, ar):
    elements = set(ar)
    total = 0
    for i in elements:
        pairs = ar.count(i) // 2
        total = total + pairs
    return total


# countingValleys #############################################################
def countingValleys(n, s):
    steps = list(map(int, s.replace("U", " 1").replace("D", " -1").split()))
    zeroCross = 0
    curHeight = 0

    for i in range(len(steps)):
        preHeight = curHeight
        curHeight = preHeight + steps[i]
        if (preHeight == 0) and (curHeight < 0):
            zeroCross = zeroCross + 1

    return zeroCross


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':

    input = [1, 2, 3, 4, 5]
    print(rotLeft([1, 2, 3, 4, 5], 4))

    input = [10, 10, 10, 20, 20, 30, 50]
    print(sockMerchant(len(input), input))

    s = "UDDDUUUUDDDU"
    print(countingValleys(len(s),s))
