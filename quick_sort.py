def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [1, 4, 8, 3, 88, 67, 93, 7, 92]
print(quick_sort(arr))




def quick_sort(arr, calls =0):
    
    calls += 1
    
    if len(arr) <= 1:
        return arr, calls
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for number in arr:
        if number < pivot:
            left.append(number)
        elif number == pivot:
            middle.append(number)

        else:
            right.append(number)

    left_sorted, calls = quick_sort(left, calls)
    right_sorted, calls = quick_sort(right, calls)


    return left_sorted + middle + right_sorted, calls


arr = [10, 7, 8, 9, 1, 90]
sorted_arr, total_calls = quick_sort(arr)
print("Відсортований масив:", sorted_arr)
print("Кількість рекурсивних викликів:", total_calls)