import math

days = int(input())
food_available = int(input())  # kg
dog_food_per_day = float(input())  # kg
cat_food_per_day = float(input())  # kg
turtle_food_per_day = float(input())  # grams

food_needed = days * (dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000)

if food_needed <= food_available:
    print(math.floor(food_available - food_needed), 'kilos of food left.')
else:
    print(math.ceil(food_needed - food_available), 'more kilos of food are needed.')
