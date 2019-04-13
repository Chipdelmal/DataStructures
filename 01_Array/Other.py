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


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':

    input = [1, 2, 3, 4, 5]
    print(rotLeft([1, 2, 3, 4, 5], 4))

    input = [10, 10, 10, 20, 20, 30, 50]
    print(sockMerchant(len(input), input))
