goal = 10000
steps_sum = 0
steps = 0

while steps_sum < goal:
    data = input()

    if data == 'Going home':
        steps = int(input())
        steps_sum += steps
        break
    else:
        steps = int(data)
        steps_sum += steps

if steps_sum >= goal:
    print('Goal reached! Good job!')
    print(f'{steps_sum - goal} steps over the goal!')
else:
    print(f'{goal - steps_sum} more steps to reach goal.')
