intervals = [(1, 3), (2, 4), (3, 5), (0, 5), (5, 7)]
intervals.sort(key=lambda x: x[1])

result = []
end_time = 0

for start, end in intervals:
    if start>= end_time:
        result.append((start, end))
        end_time = end
print("mettings:", result)

