length = int(input())
width = int(input())

total_pieces = length * width

data = input()

while data != 'STOP':
    pieces = int(data)
    total_pieces -= pieces

    if total_pieces <= 0:
        break

    data = input()

if total_pieces >= 0:
    print(f'{total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
