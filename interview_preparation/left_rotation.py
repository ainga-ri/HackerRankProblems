#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#
"""
The way we saw to solve it, is by separating sub arrays of left and right, if the example is "5 1" it's going to move only one time to the left
we separate the array 1:5 (these are positions) --> [1 2 3 4 5] --> 2 3 4 5, and 0:1 (positions) --> 1, so --> 2 3 4 5 1

We attach a file with the skecth with the algorithm represented
"""
def rotLeft(a, d):
    # Write your code here
    rotate = a[d:len(a)] + a[0:d]
    return rotate
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
