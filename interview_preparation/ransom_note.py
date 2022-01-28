#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    dict_magazine = {}
    
    for i in magazine:
        if i in dict_magazine:
            dict_magazine[i] += 1
        else:
            dict_magazine[i] = 1
    for i in note:
        if (i in dict_magazine and dict_magazine[i] != 0):
            dict_magazine[i] -= 1
        else:
           return print("No")
    
    return print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
