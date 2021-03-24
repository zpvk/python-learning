#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus,minus,zero = 0,0,0
    for i in arr:
        if i == 0:
            zero +=1
        elif i<=-1:
            minus +=1
        elif i>=1:
            plus +=1
    print("{:.6f}\n{:.6f}\n{:.6f}".format(plus/len(arr),minus/len(arr),zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
