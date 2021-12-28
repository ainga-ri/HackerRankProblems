arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sum_of_matrix = []
for i in range(4):
    for j in range(4):
        square = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +
        arr[i+2][j+0] + arr[i+2][j+1] + arr[i+2][j+2])
        sum_of_matrix.append(square)

print(max(sum_of_matrix))

