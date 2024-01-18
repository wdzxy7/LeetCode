def findMinArrowShots(self, points):
    points.sort(key=lambda x: (x[0], x[1]))
    pre_shoot = points[0]
    shoot_count = 1
    for i in range(1, len(points)):
        if points[i][0] <= pre_shoot[1]:
            pre_shoot[0] = points[i][0]
            if points[i][1] <= pre_shoot[1]:
                pre_shoot[1] = points[i][1]
        else:
            shoot_count += 1
            pre_shoot = points[i]
    return shoot_count


print(findMinArrowShots(None, [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))