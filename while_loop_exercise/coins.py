change = float(input())
n = int(change * 100)
coins_count = 0
coins = 0

while n > 0:
    if n < 1:
        break
    if n >= 200:
        coins = n // 200
        coins_count += coins
        n -= coins * 200
    elif n >= 100:
        coins = n // 100
        coins_count += coins
        n -= coins * 100
    elif n >= 50:
        coins = n // 50
        coins_count += coins
        n -= coins * 50
    elif n >= 20:
        coins = n // 20
        coins_count += coins
        n -= coins * 20
    elif n >= 10:
        coins = n // 10
        coins_count += coins
        n -= coins * 10
    elif n >= 5:
        coins = n // 5
        coins_count += coins
        n -= coins * 5
    elif n >= 2:
        coins = n // 2
        coins_count += coins
        n -= coins * 2
    else:
        coins = n // 1
        coins_count += coins
        n -= coins * 1

print(coins_count)
