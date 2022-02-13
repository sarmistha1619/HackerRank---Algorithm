#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
n = int(input())
def plusMinus(arr):
#Write your code here
    p=m=z=0
    for i in range(n):
        if arr[i]>0:
            p=p+1
        elif arr[i]<0:
            m=m+1
        else:
            z=z+1
    print(p/n)
    print(m/n)
    print(z/n)

if __name__ == '__main__':


    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
