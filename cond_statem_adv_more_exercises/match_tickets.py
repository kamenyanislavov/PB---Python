budget = float(input())
category = input()  # VIP or Normal
people_number = int(input())

transport = 0
ticket_price = 0

if 1 <= people_number <= 4:
    transport = budget * 0.75
elif 5 <= people_number <= 9:
    transport = budget * 0.60
elif 10 <= people_number <= 24:
    transport = budget * 0.50
elif 25 <= people_number <= 49:
    transport = budget * 0.40
elif people_number >= 50:
    transport = budget * 0.25

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

money_for_tickets = people_number * ticket_price

if budget >= (transport + money_for_tickets):
    print(f'Yes! You have {budget - transport - money_for_tickets:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_for_tickets + transport - budget:.2f} leva.')
