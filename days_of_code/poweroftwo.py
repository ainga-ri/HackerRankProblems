def isPowerOfTwo (x):
	# First x in the below expression
	# is for the case when x is 0
    result = x-1
    result = x & result 
    result = not(result)
    result = (x and result)
    return 1

# Driver code
if(isPowerOfTwo(9)):
	print('Yes')
else:
	print('No')
	
if(isPowerOfTwo(64)):
	print('Yes')
else:
	print('No')