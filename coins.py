coins = [1, 2, 5]
amount = 11
result = []

for coin in sorted(coins, reverse=True):
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)

another_coins = [1, 3, 4]
sum = 6
result_2 = []

for another_coin in sorted(another_coins, reverse=True):
    while sum >= another_coin:
        sum -= another_coin
        result_2.append(another_coin)
print(result_2)