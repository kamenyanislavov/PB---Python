pc_qty = int(input())  # the number of different pc models

rating = 0
possible_sales = 0
rating_sum = 0
total_sales = 0


for x in range(pc_qty):
    data = str(input())
    rating = int(data[2])
    possible_sales = int(data[0:2])

    if rating == 2:
        possible_sales *= 0 / 100
    elif rating == 3:
        possible_sales *= 50 / 100
    elif rating == 4:
        possible_sales *= 70 / 100
    elif rating == 5:
        possible_sales *= 85 / 100
    elif rating == 6:
        possible_sales *= 100 / 100

    rating_sum += rating
    total_sales += possible_sales

avg_rating = rating_sum / pc_qty

print(f'{total_sales:.2f}')
print(f'{avg_rating:.2f}')
