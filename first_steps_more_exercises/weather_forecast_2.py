temperature = float(input())

if temperature >= 26 and temperature <= 35:
    print("Hot")
elif temperature > 20 and temperature < 26:
    print("Warm")
elif temperature >= 15 and temperature <= 20:
    print("Mild")
elif temperature >= 12 and temperature < 15:
    print("Cool")
elif (temperature >= 5 and temperature < 12):
    print("Cold")
else:
    print("unknown")
