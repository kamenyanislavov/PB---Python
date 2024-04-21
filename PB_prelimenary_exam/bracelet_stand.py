pocket_money = float(input())
income_per_day = float(input())
total_costs = float(input())
present_price = float(input())

days = 5
money_saved = pocket_money * days + income_per_day * days - total_costs

if money_saved >= present_price:
    print(f'Profit: {money_saved:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {present_price - money_saved:.2f} BGN.')
