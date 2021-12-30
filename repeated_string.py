#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

"""
This function finds the letter is most repeated and NOT ONLY A
"""

def repeatedStringBetter(s, n):
    # Write your code here
    abecedary = {}
    for value in s:
        if value in abecedary:
            abecedary[value] += 1
        else:
            abecedary[value] = 1
    
            max_value = max(abecedary, key = abecedary.get) # get max value of a dictionary
    num_max_value_s = 0 # number of times the max value is in a string
    
    for i in range(len(s)):
        if (s[i] == max_value):
            num_max_value_s += 1
            
    num_max_value = n // len(s) * num_max_value_s
    
    if (n % len(s) != 0):
        rest = n % len(s)
        for i in range(0, rest):
            if (s[i] == max_value):
                num_max_value += 1
            
    return num_max_value
  
  """
  This goes HackerRank function
  """
  def repeatedString(s, n):
    
if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
