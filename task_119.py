def getRow(self, rowIndex):
    res = [1]
    for i in range(1, rowIndex + 1):
        t = [1]
        for j in range(i - 1):
            t.append(res[j] + res[j + 1])
        t.append(1)
        res = t.copy()
    return res


print(getRow(None, 1))