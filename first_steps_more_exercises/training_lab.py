import math

room_length = float(input())
room_width = float(input())

desks_per_row = (room_width * 100 - 100) / 70
rows = (room_length * 100) / 120
numer_of_desks = (math.floor(desks_per_row) * math.floor(rows)) - 3

print(numer_of_desks)
