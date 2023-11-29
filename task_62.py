def uniquePaths(self, m, n):
    step = [[0] * n for i in range(m)]
    step[0] = [1 for i in range(n)]
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                step[i][j] = step[i - 1][j]
            else:
                step[i][j] = step[i - 1][j] + step[i][j - 1]
    return step[m - 1][n - 1]

print(uniquePaths(None, 3, 7))