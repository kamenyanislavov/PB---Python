month = input()
nights = int(input())

apartment_price = 0
studio_price = 0
apartment_bill = 0
studio_bill = 0

if month == 'May' or month == 'October':
    apartment_price = 65
    studio_price = 50
    if nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
    elif nights > 7:
        studio_price *= 0.95

elif month == 'June' or month == 'September':
    apartment_price = 68.70
    studio_price = 75.20
    if nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'July' or month == 'August':
    apartment_price = 77
    studio_price = 76
    if nights > 14:
        apartment_price *= 0.90

apartment_bill = apartment_price * nights
studio_bill = studio_price * nights

print(f'Apartment: {apartment_bill:.2f} lv.')
print(f'Studio: {studio_bill:.2f} lv.')
