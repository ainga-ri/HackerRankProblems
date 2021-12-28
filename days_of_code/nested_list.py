records = []
scores = []
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append(name)
    scores.append(score)
    records.append([students[_], scores[_]])

def partition(arr, low, high):
    i = (low-1)
    pivot_number = arr[high][1]
    pivot_name = arr[high][0]
    for j in range(low, high):
        if (arr[j][1] < pivot_number or (arr[j][1] == pivot_number and arr[j][0] < pivot_name)):
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)

def quickSort(arr, low, high):
    if (len(arr) == 1):
        return arr
    if (low < high):
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(records, 0, len(records)-1)

lowest = records[0][1]
i = 1
while (lowest == records[i][1]):
    i += 1
second_lowest = records[i][1]

for i in range(len(records)):
    if(second_lowest == records[i][1]):
        print(records[i][0])
