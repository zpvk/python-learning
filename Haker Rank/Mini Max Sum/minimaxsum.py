#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)-1):
        sum1 += arr[i]
    sum2 = sum1+arr[-1]-arr[0]
    print(sum1,sum2)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
