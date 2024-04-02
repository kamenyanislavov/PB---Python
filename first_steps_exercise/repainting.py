nylon_qty = int(input())
paint_qty = int(input())
diluter = int(input())
hours_to_work = int(input())

materials_price = (nylon_qty + 2) * 1.50 + (paint_qty * 1.10) * 14.50 + diluter * 5 + 0.40
price_for_painting = materials_price * 0.30 * hours_to_work

final_price = materials_price + price_for_painting

print(final_price)
