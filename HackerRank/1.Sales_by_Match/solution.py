#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # generate the sock pair by comparing how many unique key appear in an arr
    # INPUT
    # :n --> length of ar (int)
    # :ar --> sock data (arr)
    # OUTPUT: return sock in pair (int)
    pair_dict = {}
    result = 0

    for item in range(n):
        temp = ar[item]
        if temp in pair_dict:
            pair_dict.update({temp: (pair_dict[temp] + 1)})
        else:
            pair_dict.update({temp: 1})
        
        if pair_dict[temp] % 2 == 0:
            result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
