import math
import os
import random
import re
import sys

print("Enter a value:")
number = int(input())

def if_else(number):
    if (number % 2 == 0):
        if(number in range(2,5)):
            state = "Not Weird"
        else:
            if(number in range(6,20)):
                state = "Weird"
            else:
                state = "Not Weird"
    else:
        state = "Weird"
    return state

print("Your number is " + if_else(number))