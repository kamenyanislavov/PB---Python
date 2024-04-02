import math

record = float(input())
distance = float(input())
speed_per_meter = float(input())

delay = math.floor(distance / 15) * 12.5
attempt_time = distance * speed_per_meter + delay

if attempt_time < record:
    print('Yes, he succeeded! The new world record is', '{:.2f}'.format(attempt_time), 'seconds.')
else:
    print('No, he failed! He was', '{:.2f}'.format(attempt_time - record), 'seconds slower.')
