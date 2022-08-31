#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
"""

What is important is the position of the player, we change 'step' to situate our player

"""
def jumpingOnClouds(c):
    # Write your code here
    step = 0
    jumps = 0
    while (step != (len(c)-1)):
        jumps += 1
        if (c[step+1] == 0):
            if ((step + 2 <= len(c)-1) and c[step+2] == 0):
                step += 2
            else:
                step += 1
        else:
            step += 2
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
