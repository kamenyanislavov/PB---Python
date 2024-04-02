import math

number_of_pages = int(input())
pages_per_hour = int(input())
days_to_read_the_book = int(input())

hours_per_day = number_of_pages / pages_per_hour / days_to_read_the_book

print(math.floor(hours_per_day))
