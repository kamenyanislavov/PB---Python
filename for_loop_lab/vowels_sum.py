str = input()

points = 0

for x in str:
    if x == 'a':
        points += 1
    elif x == 'e':
        points += 2
    elif x == 'i':
        points += 3
    elif x == 'o':
        points += 4
    elif x == 'u':
        points += 5

print(points)
