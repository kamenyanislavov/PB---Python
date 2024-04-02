budget = int(input())
season = input()
fishermen = int(input())

boat_rent = 0

if season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Spring':
    boat_rent = 3000
else:
    boat_rent = 2600

if fishermen <= 6:
    boat_rent *= 0.90
elif 7 <= fishermen <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if fishermen % 2 == 0 and season != 'Autumn':
    boat_rent *= 0.95

if budget >= boat_rent:
    print(f"Yes! You have {budget - boat_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rent - budget:.2f} leva.")
