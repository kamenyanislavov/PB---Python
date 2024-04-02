length = int(input())
width = int(input())
height = int(input())
percent_to_decrease = float(input())

volume_of_tank = (length * width * height) / 1000
water_needed = volume_of_tank * ((100 - percent_to_decrease) / 100)

print(water_needed)
