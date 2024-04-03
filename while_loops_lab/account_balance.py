payment = input()
total_amount = 0
num = 0

while payment != 'NoMoreMoney':
    num = float(payment)
    if num >= 0:
        total_amount += num
        print(f'Increase: {num:.2f}')
    else:
        print('Invalid operation!')
        break
    payment = input()

print(f'Total: {total_amount:.2f}')
