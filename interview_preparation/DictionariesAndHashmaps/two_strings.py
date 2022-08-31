#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# I find the first option more readable and it follows the search structure and it uses only one "return", they have the same complexity.
def twoStrings1(s1, s2):
    # Write your code here
    s1 = list(s1)
    result = "NO"
    i = 0
    while(result == "NO" and i < len(s1)):
        if s1[i] in s2:
            result = "YES"
        i += 1
    return result

def twoStrings2(s1, s2):
   # Write your code here
    for i in list(s1):
        if i in s2:
            return ("YES")
    return ("NO")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
