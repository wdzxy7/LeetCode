def jewelleryValue(self, frame):
    res = [[0 for i in range(len(frame[0]))] for i in range(len(frame))]
    res[0][0] = frame[0][0]
    for i in range(1, len(frame[0])):
        res[0][i] = res[0][i - 1] + frame[0][i]
    for i in range(1, len(frame)):
        res[i][0] = res[i - 1][0] + frame[i][0]
    for i in range(1, len(frame)):
        for j in range(1, len(frame[0])):
            res[i][j] = max(res[i - 1][j], res[i][j - 1]) + frame[i][j]
    max_value = 0
    for i in res:
        max_value = max(max_value, max(i))
    return max_value


print(jewelleryValue(None, [[1,3,1],[1,5,1],[4,2,1]]))