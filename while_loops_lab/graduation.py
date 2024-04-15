student_name = input()

fails = 0
counter = 0
grades_sum = 0

while counter < 12:
    grade = float(input())

    if grade < 4:
        fails += 1
        if fails > 1:
            print(f'{student_name} has been excluded at {counter + 1} grade')
            break
    else:
        counter += 1
        grades_sum += grade

else:
    avg_grade = grades_sum / counter
    print(f'{student_name} graduated. Average grade: {avg_grade:.2f}')
