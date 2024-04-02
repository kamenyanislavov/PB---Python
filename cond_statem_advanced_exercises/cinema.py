projection_type = input()
rows = int(input())
columns = int(input())

total_seats = rows * columns
ticket_price = 0
income = 0

if projection_type == 'Premiere':
    ticket_price = 12
elif projection_type == 'Normal':
    ticket_price = 7.50
else:
    ticket_price = 5

income = total_seats * ticket_price

print('{:.2f}'.format(income), 'leva')
