flowers = input()
flowers_qty = int(input())
budget = int(input())

price = 0
bill = 0

if flowers == 'Roses':
    price = 5
    if flowers_qty > 80:
        price *= 0.90
elif flowers == 'Dahlias':
    price = 3.80
    if flowers_qty > 90:
        price *= 0.85
elif flowers == 'Tulips':
    price = 2.80
    if flowers_qty > 80:
        price *= 0.85
elif flowers == 'Narcissus':
    price = 3
    if flowers_qty < 120:
        price *= 1.15
elif flowers == 'Gladiolus':
    price = 2.50
    if flowers_qty < 80:
        price *= 1.20

bill = flowers_qty * price

if budget >= bill:
    print(f'Hey, you have a great garden with {flowers_qty} {flowers} and {budget - bill:.2f} leva left.')
else:
    print(f'Not enough money, you need {bill - budget:.2f} leva more.')
