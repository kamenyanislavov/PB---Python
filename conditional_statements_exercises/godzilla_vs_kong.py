budget = float(input())
actors = int(input())
clothes_price = float(input())

decore = budget * 0.10
money_needed = 0

if actors > 150:
    clothes_price *= 0.90

money_needed = actors * clothes_price + decore

if money_needed > budget:
    print('Not enough money!')
    print('Wingard needs', '{:.2f}'.format(money_needed - budget), 'leva more.')
else:
    print('Action!')
    print('Wingard starts filming with', '{:.2f}'.format(budget - money_needed), 'leva left.')
