def eraseOverlapIntervals(self, intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    pre = intervals[0]
    remove_count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < pre[1]:
            remove_count += 1
            if pre[1] > intervals[i][1]:
                pre = intervals[i]
        else:
            pre = intervals[i]
    return remove_count


print(eraseOverlapIntervals(None, [[0,2],[1,3],[2,4],[3,5],[4,6]]))