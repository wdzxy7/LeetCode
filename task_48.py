def rotate(self, matrix):
    l = len(matrix[0]) - 1
    a = 0
    b = l
    while a < b:
        for i in range(a, b):
            t = matrix[a][i]
            matrix[a][i] = matrix[l - i][a]
            matrix[l - i][a] = matrix[b][l - i]
            matrix[b][l - i] = matrix[i][b]
            matrix[i][b] = t
        a += 1
        b -= 1
    return matrix
print(rotate(None,[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))