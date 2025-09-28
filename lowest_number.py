import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Вибираємо випадковий опорний елемент
    pivot = random.choice(arr)

    # Ділимо масив на три частини
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        # k-й елемент у "лівій" частині
        return quick_select(lows, k)
    elif k > len(lows) + len(pivots):
        # k-й елемент у "правій" частині
        return quick_select(highs, k - len(lows) - len(pivots))
    else:
        # k-й елемент є сам pivot
        return pivot


# Приклад використання
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}-й найменший елемент:", quick_select(arr, k))
