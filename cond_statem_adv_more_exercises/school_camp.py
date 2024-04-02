season = input()
group_type = input()
pupils_number = int(input())
nights_number = int(input())

price_per_night = 0
total_price = 0
sport = ''

if season == 'Winter':

    if group_type == 'boys':
        price_per_night = 9.60
        sport = 'Judo'

    elif group_type == 'girls':
        price_per_night = 9.60
        sport = 'Gymnastics'

    elif group_type == 'mixed':
        price_per_night = 10
        sport = 'Ski'

elif season == 'Spring':

    if group_type == 'boys':
        price_per_night = 7.20
        sport = 'Tennis'

    elif group_type == 'girls':
        price_per_night = 7.20
        sport = 'Athletics'

    elif group_type == 'mixed':
        price_per_night = 9.50
        sport = 'Cycling'

elif season == 'Summer':

    if group_type == 'boys':
        price_per_night = 15
        sport = 'Football'

    elif group_type == 'girls':
        price_per_night = 15
        sport = 'Volleyball'

    elif group_type == 'mixed':
        price_per_night = 20
        sport = 'Swimming'

if 10 <= pupils_number < 20:
    price_per_night *= 0.95

elif 20 <= pupils_number < 50:
    price_per_night *= 0.85

elif pupils_number >= 50:
    price_per_night *= 0.50

total_price = price_per_night * pupils_number * nights_number

print(f'{sport} {total_price:.2f} lv.')
