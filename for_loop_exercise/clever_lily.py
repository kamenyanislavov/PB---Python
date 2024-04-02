age = int(input())
washer_price = float(input())
toy_price = int(input())

money = 0
money_saved = 0
toys_qty = 0

for x in range(1, age + 1):

    if x % 2 != 0:
        toys_qty += 1
    else:
        money += 10
        money_saved += money - 1

money_saved = money_saved + toy_price * toys_qty

if money_saved >= washer_price:
    print(f'Yes! {money_saved - washer_price:.2f}')
else:
    print(f'No! {washer_price - money_saved:.2f}')
