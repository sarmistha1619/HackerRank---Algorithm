'''
b=int(input())
e=[]
s=0
h=0
for c in range(b):
    d=list(map(int, input().split()))
    e=e+d
if b==1:
    print(0)
elif b>1:
    for i in range(len(e)):
        if i % (b+1) == 0:
            s = s + e[i]
        elif i % (b-1) == 0:
            h = h + e[i]
    print(abs(abs(s)-abs(h-e[(b*b)-1])))
'''

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftdiag = rightdiag = 0
    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n - 1 - i]
    return abs(leftdiag - rightdiag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
