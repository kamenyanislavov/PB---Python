numbers = int(input())

odd_sum = 0
even_sum = 0

for x in range(numbers):
    num = int(input())

    if x % 2 == 0:
        odd_sum += num
    else:
        even_sum += num

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    print('No')
    print(f'Diff = {abs(odd_sum - even_sum)}')
