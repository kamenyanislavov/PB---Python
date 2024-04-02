season = input()
millage = float(input())

money_earned = 0

if millage <= 5000:

    if season == 'Spring' or season == 'Autumn':
        money_earned = 4 * (millage * 0.75) * 0.90

    elif season == 'Summer':
        money_earned = 4 * (millage * 0.90) * 0.90

    elif season == 'Winter':
        money_earned = 4 * (millage * 1.05) * 0.90

elif 5000 < millage <= 10000:

    if season == 'Spring' or season == 'Autumn':
        money_earned = 4 * (millage * 0.95) * 0.90

    elif season == 'Summer':
        money_earned = 4 * (millage * 1.10) * 0.90

    elif season == 'Winter':
        money_earned = 4 * (millage * 1.25) * 0.90

else:
    money_earned = 4 * (millage * 1.45) * 0.90

print(f'{money_earned:.2f}')
