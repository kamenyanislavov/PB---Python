num1 = int(input())
num2 = int(input())

for x in range(num1, num2 + 1):
    num_as_str = str(x)
    even_sum = 0
    odd_sum = 0
    for i in range(0, len(num_as_str)):

        if i % 2 == 0:
            even_sum += int(num_as_str[i])
        else:
            odd_sum += int(num_as_str[i])

    if even_sum == odd_sum:
        print(num_as_str, end=' ')
