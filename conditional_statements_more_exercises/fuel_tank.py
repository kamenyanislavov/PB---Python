fuel_type = input()
fuel_qty = float(input())

if (fuel_type != 'Diesel') and (fuel_type != 'Gasoline') and (fuel_type != 'Gas'):
    print('Invalid fuel!')
else:
    if fuel_qty >= 25:
        print(f'You have enough {fuel_type.lower()}.')
    else:
        print(f'Fill your tank with {fuel_type.lower()}!')
