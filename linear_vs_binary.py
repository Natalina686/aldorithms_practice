import time

def linear_search(numbers, target):
    for n in numbers:
        if n == target:
            return n
    return None


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return target
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

numbers = list(range(1, 1_000_001))
target = 999_991

start = time.time()
linear_search(numbers, target)
end = time.time()
print(f"Лінійний пошук: {end - start: 5f} секунд")

start = time.time()
binary_search(numbers, target)
end = time.time()
print(f"Бінарний пошук: {end - start: 5f} секунд")