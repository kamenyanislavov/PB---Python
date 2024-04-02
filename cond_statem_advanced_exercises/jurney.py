budget = float(input())
season = input()

place = ''
accommodation = ''
price = 0

if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.30
    else:
        accommodation = 'Hotel'
        price = budget * 0.70
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.40
    else:
        accommodation = 'Hotel'
        price = budget * 0.80
else:
    place = 'Europe'
    accommodation = 'Hotel'
    price = budget * 0.90

print(f'Somewhere in {place}')
print(f"{accommodation} - {price:.2f}")
