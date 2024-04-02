junior_bikers = int(input())
senior_bikers = int(input())
track_type = input()

money_raised = 0

if track_type == 'trail':
    money_raised = junior_bikers * 5.50 + senior_bikers * 7
elif track_type == 'cross-country':
    if (senior_bikers + junior_bikers) >= 50:
        money_raised = (junior_bikers * 8 + senior_bikers * 9.50) * 0.75
    else:
        money_raised = junior_bikers * 8 + senior_bikers * 9.50
elif track_type == 'downhill':
    money_raised = junior_bikers * 12.25 + senior_bikers * 13.75
elif track_type == 'road':
    money_raised = junior_bikers * 20 + senior_bikers * 21.50

money_raised *= 0.95

print(f'{money_raised:.2f}')
