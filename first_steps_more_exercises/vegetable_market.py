vegetable_price = float(input())
fruit_price = float(input())
vegetable_qty = int(input())
fruit_qty = int(input())

total_sum_bgn = vegetable_price * vegetable_qty + fruit_price * fruit_qty
total_sum_euro = total_sum_bgn / 1.94

print("{:.2f}".format(total_sum_euro))
