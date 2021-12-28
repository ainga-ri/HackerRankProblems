x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Multiple Loops

list_permutation = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k != n):
                list_permutation.append([i,j,k])

print(list_permutation)

# List Comprehension

listcomprehension_permutation = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k != n)]

# The first element will be the last element to iterate, list_comprehension = [operations iteration variable in ___ conditional]
# operations means what is going to do the loop
# iteration with the variable to iterate
# __ means the range or where is going to iterate the variable
# the conditions go in the final of the list comprehension

print(listcomprehension_permutation)

