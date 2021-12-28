#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    '''
    max_value = 0
    for i in range(1,N):
        for j in range(i+1,N):
            if ((i & j) < K) and ((i & j) > max_value): 
                max_value = i & j
                if (max_value == (K-1)):
                    return max_value
    return max_value
    '''
    
    if((K % 2 != 0 and K != N) or (K-1 | K) <= N):
        result = K-1
    else:
        result = K-2
    return result

    
    
    '''
    k_digit = "{0:b}".format(K & K)
    if (re.findall("1$", k_digit)):
        result = K-1
    else:
        if(K and (not(K & (K-1)))):
            result = K-1
        else:
            result = K-2
    return result
    '''

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
        print(res)
        #fptr.write(str(res) + '\n')

    #fptr.close()
