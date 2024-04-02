day_of_week = input()

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if day_of_week in weekend[0:2]:
    print("Weekend")
elif day_of_week in working_days[0:5]:
    print('Working day')
else:
    print('Error')
