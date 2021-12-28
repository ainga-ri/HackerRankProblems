# Basics of the Exceptions

S = input()
try:
    integer = int(S)
    print(integer)
except ValueError:
    print("Bad string")


# More basics of the Exceptions

class Calculator:
    def power(n, p):
        if (n < 0 or p < 0):
            raise Exception("n and p should be non-negative") # with this we provocate an Exception
        else:
            return n**p
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   