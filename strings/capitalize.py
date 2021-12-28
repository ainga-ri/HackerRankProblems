#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_s = ''
    new_s = s[0].capitalize()
    for i in range(1, len(s)):
        if(s[i-1] == ' ' and s[i] != ' '):
            new_s += s[i].capitalize()
        else:
            new_s += s[i]
    return new_s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
