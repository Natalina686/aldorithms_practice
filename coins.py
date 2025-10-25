coins = [1, 2, 5]
amount = 11
result = []

for coin in sorted(coins, reverse=True):
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)

another_coins = [1, 3, 4]
total = 6
result_2 = []

for another_coin in sorted(another_coins, reverse=True):
    while total >= another_coin:
        total -= another_coin
        result_2.append(another_coin)
        optimal = 2
print(result_2)


optimal = 2
if len(result_2) != optimal:
    print("Greedy failed - not optimal")
else:
    print("Greedy works optimally ✅")


def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
            while amount >= coin:
               amount -= coin
               result.append(coin)
    
    return result, len(result)

def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def compare_algorithms(coins, amount):
    greedy_result, greedy_count = greedy_coin_change(coins,amount)
    dp_count = dp_coin_change(coins, amount)

    print(f"Монети: {coins}, сума: {amount}")
    print(f"Greedy: {greedy_result} (кількість = {greedy_count})")
    print(f"Оптимальне (DP): {dp_count} монет")

    if greedy_count == dp_count:
        print("Greedy знайшов оптимальне рішення!")
    else:
        print("Greedy НЕ оптимальне.")



compare_algorithms([1, 2, 5], 11)
print()
compare_algorithms([1, 3, 4], 6)

coins = [1, 2, 5, 10, 20, 50]
amount = 93

result, count = greedy_coin_change(coins, amount)
print(result)
print(count)