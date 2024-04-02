house_height = float(input())
side_wall_length = float(input())
roof_height = float(input())

door_area = 1.20 * 2.00
windows_area = 2 * (1.50 * 1.50)
walls_area = (2 * (house_height * house_height) + 2 * (house_height * side_wall_length) -
              door_area - windows_area)
green_paint_qty = walls_area / 3.4

roof_area = 2 * (house_height * side_wall_length) + 2 * (house_height * roof_height / 2)
red_paint_qty = roof_area / 4.3

print("{:.2f}".format(green_paint_qty))
print("{:.2f}".format(red_paint_qty))
