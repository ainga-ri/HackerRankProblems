n = int(input())
arr = sorted(list(map(int, input().split())))
max_value = max(arr)

for i in range(n):
    if (arr[i] < max_value):
        max_second_value = arr[i]
print(max_second_value)

'''while max(arr) == max_value:
    arr.remove(max(arr))
print(max(arr))
'''
