# Ref: https://www.youtube.com/watch?v=Ik5W3OibQ2Q&ab_channel=NickWhite
# test case:
# n = 85
# c = [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
# ans: 46

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    # find the jumping point
    # if the third point is 1, we can assume there's two zeros: jump 1 && move the step by one
    # else we can skip one zero and then move 2 steps
    # INPUT
    # :n --> length of arr (int)
    # :c --> cloud path (arr)
    # OUTPUT: return minimum jump in the cumulus (int)
    ele = 0
    jump = 0

    while ele < (n - 1):
        if ele + 2 == n or c[ele + 2] == 1:
            ele += 1
            jump += 1
        else:
            ele += 2
            jump += 1
            
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
