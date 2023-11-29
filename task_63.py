def uniquePathsWithObstacles(self, obstacleGrid):
    weigh = len(obstacleGrid[0])
    high = len(obstacleGrid)
    step = [[0] * weigh for i in range(high)]
    step[0] = [1 for i in range(weigh)]
    for i in range(weigh):
        if obstacleGrid[0][i] == 1:
            for j in range(i, weigh):
                step[0][j] = 0
            break
    for i in range(1, high):
        for j in range(weigh):
            if obstacleGrid[i][j] == 1:
                step[i][j] = 0
            elif j == 0:
                step[i][j] = step[i - 1][j]
            else:
                step[i][j] = step[i - 1][j] + step[i][j - 1]
    return step[-1][-1]


print(uniquePathsWithObstacles(None, [[0,0,0],[0,1,0],[0,0,0]]))