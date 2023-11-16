import math


def countLatticePoints(self, circles):
    circles = sorted(circles, key=lambda x: (x[0], x[1]))
    point_set = set()
    above = 0
    right = 0
    for circle in circles:
        above = max(above, circle[0] + circle[2])
        right = max(right, circle[1] + circle[2])
    for i in range(above + 1):  # y
        for j in range(right + 1):  # x
            for circle in circles:
                dis = math.sqrt((circle[0] - i) ** 2 + (circle[1] - j) ** 2)
                if dis <= circle[2]:
                    point_set.add((i, j))
    return len(point_set)

print(countLatticePoints(None, [[2,2,2],[3,4,1]]))