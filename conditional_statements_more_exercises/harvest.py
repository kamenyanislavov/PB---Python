import math

vineyard_area = int(input())  # square meters of vineyard
grapes_per_sqm = float(input())  # grapes per square meter of vineyard
wine_needed = int(input())
workers = int(input())

total_harvest = vineyard_area * grapes_per_sqm
grapes_for_wine = total_harvest * 0.40
wine_produced = grapes_for_wine / 2.5

if wine_produced < wine_needed:
    print('It will be a tough winter! More', math.floor(wine_needed - wine_produced), 'liters wine needed.')
else:
    print(f'Good harvest this year! Total wine:', math.floor(wine_produced), 'liters.')
    print(math.ceil(wine_produced - wine_needed), 'liters left ->', math.ceil((wine_produced - wine_needed) / workers),
          'liters per person.')
