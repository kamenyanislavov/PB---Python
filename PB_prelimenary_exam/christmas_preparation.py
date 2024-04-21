paper_rolls = int(input())
cloth_rolls = int(input())
glue_litters = float(input())
discount = int(input())

bill = (paper_rolls * 5.80 + cloth_rolls * 7.20 + glue_litters * 1.20)
final_bill = bill - (bill * discount / 100)

print(f'{final_bill:.3f}')
