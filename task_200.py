import queue


def numIslands(self, grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[0 for i in range(w)] for i in range(h)]
    count = 0
    search_queue = queue.Queue()
    for i in range(h):
        for j in range(w):
            if visited[i][j] or grid[i][j] == '0':
                continue
            search_queue.put((i, j))
            count += 1
            while not search_queue.empty():
                node = search_queue.get()
                if visited[node[0]][node[1]]:
                    continue
                # up
                if node[0] - 1 >= 0:
                    if grid[node[0] - 1][node[1]] == '1':
                        search_queue.put((node[0] - 1, node[1]))
                # down
                if node[0] + 1 < h:
                    if grid[node[0] + 1][node[1]] == '1':
                        search_queue.put((node[0] + 1, node[1]))
                # right
                if node[1] + 1 < w:
                    if grid[node[0]][node[1] + 1] == '1':
                        search_queue.put((node[0], node[1] + 1))
                if node[1] - 1 >= 0:
                    if grid[node[0]][node[1] - 1] == '1':
                        search_queue.put((node[0], node[1] - 1))
                visited[node[0]][node[1]] = 1
    return count



print(numIslands(None, [["1","1","1"],["0","1","0"],["1","1","1"]]))