mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())

bonito_bill = bonito_kg * (mackerel_price * 1.60)
scad_bill = scad_kg * (sprinkle_price * 1.80)
mussels_bill = mussels_kg * 7.50

total_bill = bonito_bill + scad_bill + mussels_bill

print("{:.2f}".format(total_bill))
