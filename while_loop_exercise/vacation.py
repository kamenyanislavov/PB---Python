money_needed = float(input())
money_saved = float(input())
action = input()
amount = float(input())

spend_days = 0
days_count = 0

while spend_days < 5:

    if action == 'save':
        money_saved += amount
        days_count += 1
        spend_days = 0

    if action == 'spend':
        if amount > money_saved:
            money_saved = 0
        else:
            money_saved -= amount
        spend_days += 1
        days_count += 1

    if money_saved >= money_needed or spend_days == 5:
        break

    action = input()
    amount = float(input())

if spend_days == 5:
    print('You can\'t save the money.')
    print(f'{days_count}')
else:
    print(f'You saved the money for {days_count} days.')
