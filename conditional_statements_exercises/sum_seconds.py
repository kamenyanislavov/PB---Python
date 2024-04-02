first_time = int(input())  # time of first player in seconds
second_time = int(input())
third_time = int(input())

total_time_seconds = first_time + second_time + third_time
minutes = total_time_seconds // 60
seconds = total_time_seconds - (minutes * 60)

if seconds > 9:
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")
