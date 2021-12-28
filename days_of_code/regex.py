#!/bin/python3

import math
import os
import random
import re
import sys

import time

def main():
    N = int(input().strip())
    names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if (re.findall("@gmail.com$", emailID)):
            names.append(firstName)
            names.sort()

    for i in range(len(names)):
        print(names[i])
    
    # or equivalent...
    # The * opens de package, without it would be [2, 3, 4] instead of 2 3 4, we also put
    # sep='\n' for printing in diferents lines, without it would be everything in one line.
    print(*sorted(names), sep='\n')

    # Question, with the two last sentences of code, which one costs more? in terms of Complexity?

# I wanted to try wich one takes less time but it depends on the time of the input, and that is not valid
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
