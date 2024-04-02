chrysanthemum_qty = int(input())
roses_qty = int(input())
tulips_qty = int(input())
season = input()
holiday = input()

is_holiday = ''
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
bill = 0

if holiday == 'Y':
    is_holiday = True
else:
    is_holiday = False

if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bill = chrysanthemum_qty * chrysanthemum_price + roses_qty * roses_price + tulips_qty * tulips_price

if is_holiday:
    bill *= 1.15

if season == 'Spring' and tulips_qty > 7:
    bill *= 0.95
elif season == 'Winter' and roses_qty >= 10:
    bill *= 0.90

if (chrysanthemum_qty + roses_qty + tulips_qty) > 20:
    bill *= 0.80
bill += 2

print(f'{bill:.2f}')
