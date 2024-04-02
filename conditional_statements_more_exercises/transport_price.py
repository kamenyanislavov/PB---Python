distance = int(input())  # distance in km
time_of_day = input()

if distance >= 100:
    price = distance * 0.06
elif distance >= 20:
    price = distance * 0.09
else:
    if time_of_day == 'day':
        price = 0.70 + distance * 0.79
    else:
        price = 0.70 + distance * 0.90

print('{:.2f}'.format(price))
