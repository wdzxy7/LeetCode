def numberOfBoomerangs(self, points):
    res = 0
    for p in points:
        temp = dict()
        for q in points:
            dis = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
            try:
                temp[dis] += 1
            except:
                temp[dis] = 1
        for v in temp.values():
            res += v * (v - 1)
    return res

print(numberOfBoomerangs(None, [[0,0],[1,0],[2,0]]))