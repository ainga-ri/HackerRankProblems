import math

def num_prime(number):
    if (number == 1):
        return "Not prime"
    else:
        for j in range(2, int(math.sqrt(number))+1):
            if(number % j == 0):
                return "Not prime"
        return "Prime"

n = int(input())
numbers = []
for i in range(n):
    pos_prime = int(input())
    print(num_prime(pos_prime))