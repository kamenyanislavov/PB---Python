profit_goal = int(input())

service_type = input()
income = 0

while service_type != 'closed':
    service_variant = input()

    if service_variant == 'mens':
        income += 15
    elif service_variant == 'ladies' or service_variant == 'touch up':
        income += 20
    elif service_variant == 'kids':
        income += 10
    elif service_variant == 'full color':
        income += 30

    if income >= profit_goal:
        break

    service_type = input()

if income >= profit_goal:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {profit_goal - income}lv. more.')
print(f'Earned money: {income}lv.')
