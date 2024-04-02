import math

radius = float(input())
r = radius

circle_area = math.pi * r * r
circle_perimeter = 2 * math.pi * r

print("{:.2f}".format(circle_area))
print("{:.2f}".format(circle_perimeter))
