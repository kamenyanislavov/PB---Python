jury_people = int(input())

total_sum_grades = 0.00  # the sum of all grades
total_average = 0.00  # for all presentations
grades_counter = 0

presentation_name = input()

while presentation_name != 'Finish':
    sum_grades = 0.00  # the sum of grades for one presentation
    avg_grade = 0.00  # for one presentation

    for x in range(1, jury_people + 1):
        grade = float(input())
        sum_grades += grade
        total_sum_grades += grade
        grades_counter += 1

    avg_grade = sum_grades / jury_people
    print(f'{presentation_name} - {avg_grade:.2f}.')
    presentation_name = input()
    
total_average = total_sum_grades / grades_counter
print(f"Student's final assessment is {total_average:.2f}.")
