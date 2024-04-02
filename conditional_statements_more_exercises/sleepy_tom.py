holidays = int(input())

play_time = (365 - holidays) * 63 + holidays * 127

if play_time <= 30000:
    hours = (30000 - play_time) // 60
    minutes = 30000 - play_time - hours * 60
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    hours = (play_time - 30000) // 60
    minutes = play_time - 30000 - hours * 60
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
