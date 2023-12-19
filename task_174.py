def calculateMinimumHP(self, dungeon):
    h = len(dungeon)
    w = len(dungeon[0])
    dp = [[1 for i in range(w)] for i in range(h)]
    dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
    # 竖着
    for i in range(h - 2, -1, -1):
        dp[i][w - 1] = max(dp[i + 1][w - 1] - dungeon[i][w - 1], 1)
    for i in range(w - 2, -1, -1):
        dp[h - 1][i] = max(dp[h - 1][i + 1] - dungeon[h - 1][i], 1)
    for i in range(h - 2, -1, -1):
        for j in range(w - 2, -1, -1):
            dp[i][j] = min(max(dp[i + 1][j] - dungeon[i][j], 1),  max(dp[i][j + 1] - dungeon[i][j], 1))
    return dp[0][0]

print(calculateMinimumHP(None, [[0]]))