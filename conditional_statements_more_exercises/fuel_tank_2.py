fuel_type = input()
fuel_qty = float(input())
club_card = input()

fuel_bill = 0

if fuel_type == 'Diesel':
    if club_card == 'Yes':
        fuel_bill = fuel_qty * (2.33 - 0.12)
    else:
        fuel_bill = fuel_qty * 2.33
elif fuel_type == 'Gasoline':
    if club_card == "Yes":
        fuel_bill = fuel_qty * (2.22 - 0.18)
    else:
        fuel_bill = fuel_qty * 2.22
elif fuel_type == 'Gas':
    if club_card == 'Yes':
        fuel_bill = fuel_qty * (0.93 - 0.08)
    else:
        fuel_bill = fuel_qty * 0.93

if 20 <= fuel_qty <= 25:
    fuel_bill *= 0.92
elif fuel_qty > 25:
    fuel_bill *= 0.90

print('{:.2f}'.format(fuel_bill), 'lv.')
