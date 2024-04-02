actor_name = input()
academy_points = float(input())
judges_number = int(input())

for x in range(judges_number):
    judge_name = input()
    judge_points = float(input())

    academy_points += (len(judge_name) * judge_points) / 2

    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!')
