chicken_menus_qty = int(input())
fish_menus_qty = int(input())
vegetarian_menus_qty = int(input())

menus_price = chicken_menus_qty * 10.35 + fish_menus_qty * 12.40 + vegetarian_menus_qty * 8.15
dessert_price = menus_price * 0.20
final_bill = menus_price + dessert_price + 2.50

print(final_bill)
