width = int(input())
length = int(input())
height = int(input())

empty_volume = width * length * height

data = input()

while data != 'Done':
    box_qty = int(data)
    empty_volume -= box_qty

    if empty_volume <= 0:
        break

    data = input()

if empty_volume >= 0:
    print(f'{empty_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(empty_volume)} Cubic meters more.')
