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
