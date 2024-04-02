budget = float(input())
videocards_qty = int(input())
processors_qty = int(input())
ram_qty = int(input())

videocard_price = 250
processor_price = videocards_qty * videocard_price * 0.35
ram_price = videocards_qty * videocard_price * 0.10
bill = videocards_qty * videocard_price + processors_qty * processor_price + ram_qty * ram_price

if videocards_qty > processors_qty:
    bill *= 0.85

if budget >= bill:
    print('You have', '{:.2f}'.format(budget - bill), 'leva left!')
else:
    print('Not enough money! You need', '{:.2f}'.format(bill - budget), 'leva more!')
