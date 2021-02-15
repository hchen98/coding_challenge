# Ref: https://www.youtube.com/watch?v=MMmFELo0QjM&ab_channel=JAVAAID-CodingInterviewPreparation
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
  # count how many times does the hiker complete one valley hike
  # if U == 0 and came back from the sea level, one valley hike complete
  # INPUT
  # :steps --> how many hikes in the path (int)
  # :path --> hike pattern (str)
  # OUTPUT: return complete valley hike (int)

    fields = map(str, path)
    result = 0

    step = 0

    for item in fields:

        if item == "D":
            step -= 1
        else:
            step += 1
            if step == 0:
                result += 1

    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
