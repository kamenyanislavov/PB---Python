import math

numbers = int(input())

max_num = - math.inf
min_num = math.inf

for n in range(numbers):

    num = int(input())

    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
