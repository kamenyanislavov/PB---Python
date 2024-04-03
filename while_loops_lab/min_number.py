n = input()
num = int(n)
min_number = num

while n != 'Stop':

    num = int(n)
    if num < min_number:
        min_number = num

    n = input()

print(min_number)
