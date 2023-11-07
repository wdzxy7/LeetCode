def merge(self, intervals):
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

print(merge(None, [[1,3],[3, 6]]))