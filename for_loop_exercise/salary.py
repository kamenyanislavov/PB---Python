tabs_num = int(input())  # open tabs in the browser
salary = int(input())

for x in range(tabs_num):
    open_site = input()

    if open_site == 'Facebook':
        salary -= 150
    elif open_site == 'Instagram':
        salary -= 100
    elif open_site == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)
