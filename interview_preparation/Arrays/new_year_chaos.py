#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    repeated = {}
    it = 0
    result = ""
    while (result != "Too chaotic" and it != len(q)-1):
        if (it+1 != q[it] and q[it] > q[it+1]):
            bribe = q[it]
            q[it], q[it+1] = q[it+1], q[it]
            if bribe in repeated:
                repeated[bribe] += 1
                if (repeated[bribe] == 3):
                    result = "Too chaotic"
            else:
                repeated[bribe] = 1
            if it != 0:
                it = it-1
        else:
            it += 1
    if (result != "Too chaotic"):
        result = sum(repeated.values())
    return print(result)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
