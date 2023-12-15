def generate(self, numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    length = 2
    for i in range(numRows - 2):
        t = [1]
        for num in range(length - 1):
            t.append(res[-1][num] + res[-1][num + 1])
        t.append(1)
        res.append(t)
        length += 1
    return res

print(generate(None, 5))