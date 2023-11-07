def spiralOrder(self, matrix):
    res = []
    a_s = 0
    a_end = len(matrix[0]) - 1
    b_s = 0
    b_end = len(matrix) - 1
    if a_s == a_end:
        res = [i[0] for i in matrix]
        return res
    elif b_s == b_end:
        return matrix[0]
    while a_s <= a_end and b_s <= b_end:
        for i in range(a_s, a_end + 1):
            res.append(matrix[b_s][i])
        for i in range(b_s + 1, b_end + 1):
            res.append(matrix[i][a_end])
        if a_s < a_end and b_s < b_end:
            for i in range(a_end - 1, a_s, -1):
                res.append(matrix[b_end][i])
            for i in range(b_end, b_s, -1):
                res.append(matrix[i][a_s])
        a_s += 1
        a_end -= 1
        b_s += 1
        b_end -= 1
    if a_s == b_s == b_end == a_end:
        res.append(matrix[a_s][a_end])
    return res


print(spiralOrder(None, [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))