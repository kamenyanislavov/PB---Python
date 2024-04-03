n = input()
num = int(n)
max_number = num

while n != 'Stop':
    num = int(n)
    if num > max_number:
        max_number = num
    n = input()

print(max_number)
