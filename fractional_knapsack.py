def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining_capacity = capacity
    taken_items = []

    for value, weight in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
            taken_items.append((value, weight, 1.0))
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            taken_items.append((value, weight, round(fraction, 2)))
            remaining_capacity = 0

    return total_value, taken_items

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

max_value, taken = fractional_knapsack(items, capacity)
print("Максимальна вартість:", max_value)
print("Взяли предмети:", taken)

assert round(fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50)[0], 2) == 240.0
print("✅ Tests passed!")

