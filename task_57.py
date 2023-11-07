def insert(self, intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x: x[0])
    res_list = []
    s = intervals[0][0]
    end = intervals[0][1]
    del intervals[0]
    for inter in intervals:
        if inter[0] <= end:
            if inter[1] > end:
                end = inter[1]
        else:
            res_list.append([s, end])
            s = inter[0]
            end = inter[1]
    res_list.append([s, end])
    return res_list

print(insert(None, [[2,5],[6,7],[8,9]], [0,1]))