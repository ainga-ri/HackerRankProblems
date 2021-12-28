final_list = []
n = int(input("Write a value: "))

for i in range(0,n):
    command = list(input("").strip().split())
    if (command[0] == 'insert'):
        final_list.insert(int(command[1]), int(command[2]))
    elif (command[0] == 'print'):
        print(final_list)
    elif (command[0] == 'remove'):
        final_list.remove(int(command[1]))
    elif (command[0] == 'append'):
        final_list.append(int(command[1]))
    elif (command[0] == 'sort'):
        final_list.sort()
    elif (command[0] == 'pop'):
        final_list.pop()
    else:
        final_list.reverse()

# IMPORTANT THEORY

"""
Yeah, I love Python one liners.

Let us break it down.
"""

input()

# This is used to fetch input from the user. In this case. We are expecting the user to provide a list of integers. 
# How do I know? Look next.

input().strip() 
 
# This will eliminate trailing spaces from the user input, if they are there. Why is it required? 
# Because some users will do that and that might break your program.
# Remember that input() will cast the input as string. So, now we have a string of integers like so: “1 2 4 42”

input.strip().split() 
 
# split() is used to create a Python list out of a string. If no delimiter is given, this breaks the string by spaces.
# So, now we have: [“1”, “2”, “4”, “42”]

map(int, input().strip().split())

# map() takes two arguments. The first one is the method to apply, the second one is the data to apply it to. 
# By this understanding, we can see this is doing nothing but typecasting every element of the list to an integer value. 
# Since map returns the data type it was applied to, the list() method applied over map() is redundant. 
# So now we have covered the following:

list(map(int, input().strip().split())) 

# And we have: [1, 2, 4, 42]

# Note the missing quotes. This means the elements are now all int.

# Now, the last bit.

I = 4
list(map(int, input().strip().split()))[:I]

"""
takes the list we have obtained and returns only the first I elements.

Neat. Right?
"""