pen_packages = int(input())
marker_packages = int(input())
detergent_litters = int(input())
discount_percent = int(input())

total_bill = pen_packages * 5.80 + marker_packages * 7.20 + detergent_litters * 1.20
discount = total_bill * discount_percent / 100
final_bill = total_bill - discount

print(final_bill)
