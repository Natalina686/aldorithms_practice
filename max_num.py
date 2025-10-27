numbers = [1,5,6,3,90,8,9,7,10]

max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number


print(max_number)

prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0

for price in prices:
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
    if price < min_price:
        min_price = price

print(max_profit)
