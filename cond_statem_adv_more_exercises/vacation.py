budget = float(input())
season = input()

accommodation = ''
price = 0
place = ''

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        price = budget * 0.65
        place = 'Alaska'
    elif season == 'Winter':
        price = budget * 0.45
        place = 'Morocco'

elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        price = budget * 0.80
        place = 'Alaska'
    elif season == 'Winter':
        price = budget * 0.60
        place = 'Morocco'

else:
    accommodation = 'Hotel'
    if season == 'Summer':
        price = budget * 0.90
        place = 'Alaska'
    elif season == 'Winter':
        price = budget * 0.90
        place = 'Morocco'

print(f'{place} - {accommodation} - {price:.2f}')
