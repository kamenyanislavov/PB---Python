destination = input()
budget = float(input())

money_saved = 0
current_sum = float(input())

while money_saved < budget:
    money_saved += current_sum

    if money_saved >= budget:
        print(f'Going to {destination}!')
        money_saved = 0
        destination = input()
        if destination == 'End':
            break
        budget = float(input())

    current_sum = float(input())
