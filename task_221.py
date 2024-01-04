def maximalSquare(self, matrix):
    dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    dp[0] = [int(i) for i in matrix[0]]
    for i in range(len(matrix)):
        dp[i][0] = int(matrix[i][0])
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == '0':
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    res = 0
    for i in dp:
        res = max(res, max(i))
    return res ** 2

print(maximalSquare(None, [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))