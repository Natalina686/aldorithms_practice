import random
import time

def counting_sort(arr):
    
    if not arr:
        return [], 0
    
    operations = 0
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        operations += 1

    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
        operations += freq

    return sorted_arr, operations

arr = [4, 2, 2, 2, 8, 3, 3, 1]
sorted_arr, ops = counting_sort(arr)
print("Відсортований масив:", sorted_arr)
print("Кількість операцій:", ops)

large_arr = [random.randint(0, 1000) for _ in range(100_000)]

start = time.time()
counting_sort(large_arr)
end = time.time()
print(f"Counting Sort час виконання: {end - start:.5f} сек.")

start = time.time()
sorted(large_arr)
end = time.time()
print(f"Built-in sorted() час виконання: {end - start:.5f} сек.")
