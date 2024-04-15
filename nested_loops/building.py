floors = int(input())
rooms_per_floor = int(input())
output = ''

for x in range(floors, 0, - 1):
    for y in range(0, rooms_per_floor, 1):

        if x == floors:
            output += f'L{x}{y} '
        elif x % 2 == 0:
            output += f'O{x}{y} '
        else:
            output += f'A{x}{y} '

    print(output)
    output = ''
