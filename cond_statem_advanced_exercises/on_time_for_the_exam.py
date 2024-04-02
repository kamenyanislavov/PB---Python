exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_tot_min = exam_hour * 60 + exam_minutes
arrival_tot_min = arrival_hour * 60 + arrival_minutes
min_diff = exam_tot_min - arrival_tot_min

if min_diff < 0:
    print('Late')
elif min_diff > 30:
    print('Early')
else:
    print('On time')

if min_diff < 0:
    if min_diff > -60:
        print(f'{abs(min_diff)} minutes after the start')
    else:
        if 0 >= (min_diff % -60) >= -9:
            print(f'{abs(min_diff) // 60}:0{abs(min_diff) % 60} hours after the start')
        else:
            print(f'{abs(min_diff) // 60}:{abs(min_diff) % 60} hours after the start')
elif min_diff > 0:
    if min_diff < 60:
        print(f'{min_diff} minutes before the start')
    else:
        if (min_diff % 60) <= 9:
            print(f'{min_diff // 60}:0{min_diff % 60} hours before the start')
        else:
            print(f'{min_diff // 60}:{min_diff % 60} hours before the start')
