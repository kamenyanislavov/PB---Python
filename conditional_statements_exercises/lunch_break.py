import math

movie_name = input()
episode_length = int(input())
lunch_break_time = int(input())

time_for_lunch = lunch_break_time / 8
time_for_rest = lunch_break_time / 4
time_left = lunch_break_time - time_for_lunch - time_for_rest

if time_left >= episode_length:
    print(f'You have enough time to watch {movie_name} and left with', math.ceil(time_left - episode_length),
          'minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need", math.ceil(episode_length - time_left),
          'more minutes.')
