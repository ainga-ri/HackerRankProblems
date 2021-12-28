n = int(input().strip())
number = ''
while (n // 2 != 0):
    rest = n % 2
    number += str(rest)
    n = n // 2
number += '1'

bigger_numbers = []
consecutive_ones = 0
for i in number:
    if (i == '1'):
        consecutive_ones += 1
    else:
        bigger_numbers.append(consecutive_ones)
        consecutive_ones = 0
bigger_numbers.append(consecutive_ones)
print(max(bigger_numbers))