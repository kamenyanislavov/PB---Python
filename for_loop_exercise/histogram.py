numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for x in range(numbers):
    num = int(input())

    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / numbers * 100:.2f}%')
print(f'{p2 / numbers * 100:.2f}%')
print(f'{p3 / numbers * 100:.2f}%')
print(f'{p4 / numbers * 100:.2f}%')
print(f'{p5 / numbers * 100:.2f}%')
