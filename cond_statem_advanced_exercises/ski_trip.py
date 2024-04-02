days = int(input())
type_of_room = input()
feedback = input()  # positive or negative

bill = 0
price = 0  # price per night

if type_of_room == 'room for one person':
    price = 18
elif type_of_room == 'apartment':
    price = 25
    if days < 10:
        price *= 0.70
    elif days > 15:
        price *= 0.50
    else:
        price *= 0.65
elif type_of_room == 'president apartment':
    price = 35
    if days < 10:
        price *= 0.90
    elif days > 15:
        price *= 0.80
    else:
        price *= 0.85

bill = price * (days - 1)

if feedback == 'positive':
    bill *= 1.25
elif feedback == 'negative':
    bill *= 0.90

print(f'{bill:.2f}')
