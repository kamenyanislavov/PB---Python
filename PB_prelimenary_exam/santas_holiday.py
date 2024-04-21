days = int(input())
room_type = input()
feedback = input()

price = 0
bill = 0

if room_type == 'room for one person':
    price = 18.00
    bill = (days - 1) * price
elif room_type == 'apartment':
    price = 25.00
    if days < 10:
        bill = (days - 1) * price * 0.7
    elif days < 15:
        bill = (days - 1) * price * 0.65
    else:
        bill = (days - 1) * price * 0.5
elif room_type == 'president apartment':
    price = 35.00
    if days < 10:
        bill = (days - 1) * price * 0.9
    elif days < 15:
        bill = (days - 1) * price * 0.85
    else:
        bill = (days - 1) * price * 0.8

if feedback == 'positive':
    bill *= 1.25
elif feedback == 'negative':
    bill *= 0.9

print(f'{bill:.2f}')
