import math

numbers = int(input())

max_num = -math.inf
total = 0

for x in range(numbers):
    num = int(input())
    if num > max_num:
        max_num = num

    total += num

if (total - max_num) == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (total - max_num))}')
