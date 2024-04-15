destination = input()
money_saved = 0

while destination != 'End':
    budget = float(input())

    while money_saved < budget:
        current_sum = float(input())
        money_saved += current_sum
    else:
        print(f'Going to {destination}!')
        money_saved = 0
        destination = input()
