#intervals = [(1, 3), (2, 5), (0, 2), (4, 6)]
#intervals.sort(key=lambda x: x[0])
#print(intervals)
#intervals.sort(key=lambda x: x[1] + x[0])
#print(intervals)

#intervals = [(5, 9), (1, 3), (2, 6), (8, 10), (0, 4)]
#print(sorted(intervals, key=lambda x: x[0]))
#print(sorted(intervals, key=lambda x: x[1]))
#print(sorted(intervals, key=lambda x: x[1] - x[0]))

intervals = [(5, 9), (1, 3), (2, 6), (8, 10), (0, 4)]
intervals.sort(key=lambda x: (x[1] - x[0], x[1]))
print(intervals)


def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    last_finish = activities[0][1]

    for start, finish in activities[1:]:
        if start >= last_finish:
            result.append((start, finish))
            last_finish = finish
    return result

activities = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
print(activity_selection(activities))

def activity_selection(activities):
    # Додаємо індекси, щоб потім знати, яка активність була яка
    indexed = list(enumerate(activities))
    
    # Сортуємо за часом завершення
    indexed.sort(key=lambda x: x[1][1])
    
    selected = []
    last_finish = 0

    for index, (start, finish) in indexed:
        if start >= last_finish:
            selected.append(index)
            last_finish = finish
    
    return selected

activities = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
result = activity_selection(activities)
print(result)

assert activity_selection([(1,2), (3,4), (0,6), (5,7), (8,9)]) == [0, 1, 3, 4]
print("✅ Tests passed!")
