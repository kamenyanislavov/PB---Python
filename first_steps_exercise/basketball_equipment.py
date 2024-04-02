annual_fee = int(input())

sneakers_price = annual_fee * 0.60
outfit_price = sneakers_price * 0.80
ball_price = outfit_price * 0.25
accessories_price = ball_price / 5

final_sum = annual_fee + sneakers_price + outfit_price + ball_price + accessories_price

print(final_sum)
