import math

tournaments_number = int(input())
start_points = int(input())  # initial number of points

wins_count = 0
points_won = 0

for x in range(tournaments_number):
    stage = input()  # the stage of tournament the tennis player reached

    if stage == 'W':
        points_won += 2000
        wins_count += 1
    elif stage == 'F':
        points_won += 1200
    elif stage == 'SF':
        points_won += 720

print(f'Final points: {start_points + points_won}')
print(f'Average points: {math.floor(points_won / tournaments_number)}')
print(f'{wins_count / tournaments_number * 100:.2f}%')
