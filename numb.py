

numbers = [2, 4, 7, 10, 14, 18, 21, 25]

my_number = 18

for number in numbers:
        if number == my_number:
            print(my_number)



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
                  
numbers = [2, 4, 7, 10, 14, 18, 21, 25] 
targets = [2, 18, 25, 100]

for t in targets:
  result = binary_search(numbers, t)
  if result is not None:
      print(f"Знайдено: {result}")
  else:
      print("Eлемент не знайдено")
