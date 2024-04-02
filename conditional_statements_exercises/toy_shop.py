excursion_price = float(input())
puzzle_qty = int(input())
dolls_qty = int(input())
teddy_bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

bill = puzzle_qty * 2.60 + dolls_qty * 3 + teddy_bears_qty * 4.10 + minions_qty * 8.20 + trucks_qty * 2
toys_qty = puzzle_qty + dolls_qty + teddy_bears_qty + minions_qty + trucks_qty

if toys_qty >= 50:
    bill *= 0.75

rent = bill * 0.10
income = bill - rent

if income >= excursion_price:
    print('Yes!', '{:.2f}'.format(income - excursion_price), 'lv left.')
else:
    print('Not enough money!', '{:.2f}'.format(excursion_price - income), 'lv needed.')
