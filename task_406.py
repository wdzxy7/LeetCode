def reconstructQueue(self, people):
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res
    for p in people:
        i = 0
        count = 0
        while i < len(res):
            if count == p[1]:
                break
            if res[i][0] >= p[0]:
                count += 1
            i += 1
        res.insert(i, p)
    return res


print(reconstructQueue(None, [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))