import math
figure_type = input()
area = 0

if figure_type == "square":
    a = float(input())
    area = a * a
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure_type == "circle":
    r = float(input())
    area = math.pi * (r ** 2)
elif figure_type == "triangle":
    a = float(input())
    h_a = float(input())
    area = (a * h_a) / 2

print("{:.3f}".format(area))
