city = input()
turnover = float(input())

cities = ['Sofia', 'Varna', 'Plovdiv']
comission = 0
income = 0
is_error = False

if city not in cities or turnover < 0:
    is_error = True
else:
    if city == 'Sofia':
        if 0 <= turnover <= 500:
            comission = 5 / 100
        elif 500 < turnover <= 1000:
            comission = 7 / 100
        elif 1000 < turnover <= 10000:
            comission = 8 / 100
        else:
            comission = 12 / 100
    elif city == 'Varna':
        if 0 <= turnover <= 500:
            comission = 4.5 / 100
        elif 500 < turnover <= 1000:
            comission = 7.5 / 100
        elif 1000 < turnover <= 10000:
            comission = 10 / 100
        else:
            comission = 13 / 100
    elif city == 'Plovdiv':
        if 0 <= turnover <= 500:
            comission = 5.5 / 100
        elif 500 < turnover <= 1000:
            comission = 8 / 100
        elif 1000 < turnover <= 10000:
            comission = 12 / 100
        else:
            comission = 14.5 / 100

income = turnover * comission

if is_error:
    print('error')
else:
    print('{:.2f}'.format(income))
