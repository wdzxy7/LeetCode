def setZeroes(self, matrix):
    h = len(matrix)
    w = len(matrix[0])
    change = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                change.append((i, j))
    for c in change:
        for i in range(h):
            matrix[i][c[1]] = 0
        for j in range(w):
            matrix[c[0]][j] = 0
    return matrix

print(setZeroes(None, [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))