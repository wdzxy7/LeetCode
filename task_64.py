def minPathSum(self, grid):
    w = len(grid[0])
    h = len(grid)
    way_sum = [[0] * w for i in range(h)]
    way_sum[0] = grid[0]
    for i in range(1, w):
        way_sum[0][i] = way_sum[0][i] + way_sum[0][i - 1]
    for i in range(1, h):
        for j in range(w):
            if j == 0:
                way_sum[i][j] = way_sum[i - 1][j] + grid[i][j]
            else:
                way_sum[i][j] = min(way_sum[i - 1][j], way_sum[i][j - 1]) + grid[i][j]
    return way_sum[-1][-1]

print(minPathSum(None, [[1,3,1],[1,5,1],[4,2,1]]))