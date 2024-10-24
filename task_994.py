import copy
import queue
from typing import List


def orangesRotting(self, grid: List[List[int]]) -> int:
    height = len(grid)
    width = len(grid[0])
    bad_orange = queue.Queue()
    dp = [[float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                bad_orange.put((i, j))
                dp[i][j] = 0
    while not bad_orange.empty():
        t_queue = queue.Queue()
        while not bad_orange.empty():
            orange = bad_orange.get()
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if (orange[0] + i == height or orange[0] + i < 0 or orange[1] + j == width or orange[1] + j < 0 or
                    grid[orange[0] + i][orange[1] + j] == 0 or grid[orange[0] + i][orange[1] + j] == 2):
                    continue
                else:
                     grid[orange[0] + i][orange[1] + j] = 2
                     t_queue.put((orange[0] + i, orange[1] + j))
                     dp[orange[0] + i][orange[1] + j] = min(dp[orange[0] + i][orange[1] + j], dp[orange[0]][orange[1]]) + 1
        while not t_queue.empty():
            bad_orange.put(t_queue.get())
    res = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return -1
            if dp[i][j] == float('inf'):
                dp[i][j] = 0
    for line in dp:
        res = max(res, max(line))
    return res

print(orangesRotting(None, [[0, 2]]))