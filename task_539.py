def findMinDifference(self, timePoints):
    timePoints = sorted(timePoints, key=lambda x: (x[0], x[1], x[3], x[4]))
    min_diff = float('inf')
    for i in range(len(timePoints)):
        if i == 0:
            diff = min(int(timePoints[0][:2]) * 60 + int(timePoints[0][3:]) + 24 * 60 - int(timePoints[-1][:2]) * 60 - int(timePoints[-1][3:]),
                       abs(int(timePoints[0][:2]) * 60 + int(timePoints[0][3:]) - (int(timePoints[-1][:2]) * 60 + int(timePoints[-1][3:]))))
        else:
            diff = abs((int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])) - (int(timePoints[i - 1][:2]) * 60 + int(timePoints[i - 1][3:])))
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(findMinDifference(None, ["01:01","02:01","03:00"]))