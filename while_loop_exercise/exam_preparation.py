poor_grades = int(input())
task_name = input()
task_grade = int(input())

last_task_name = task_name
poor_grades_counter = 0
grade_sum = 0
grade_count = 0
avg_grade = 0

while task_name != 'Enough':

    if task_grade <= 4:
        poor_grades_counter += 1

    if poor_grades_counter == poor_grades:
        break

    grade_count += 1
    grade_sum += task_grade
    last_task_name = task_name

    task_name = input()
    if task_name == 'Enough':
        break
    task_grade = int(input())

if poor_grades_counter == poor_grades:
    print(f'You need a break, {poor_grades} poor grades.')
else:
    print(f'Average score: {grade_sum / grade_count:.2f}')
    print(f'Number of problems: {grade_count}')
    print(f'Last problem: {last_task_name}')
