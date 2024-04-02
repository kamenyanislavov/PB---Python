import math

magnolia_qty = int(input())
hyacinth_qty = int(input())
rose_qty = int(input())
cactus_qty = int(input())
gift_price = float(input())

money_won = (magnolia_qty * 3.25 + hyacinth_qty * 4 + rose_qty * 3.50 + cactus_qty * 8) * 0.95

if money_won >= gift_price:
    print('She is left with', math.floor(money_won - gift_price), 'leva.')
else:
    print('She will have to borrow', math.ceil(gift_price - money_won), 'leva.')
