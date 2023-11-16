def minScore(self, n, roads):
    import queue
    matrix = [[] for i in range(n)]
    for road in roads:
        matrix[road[0] - 1].append((road[1] - 1, road[2]))
        matrix[road[1] - 1].append((road[0] - 1, road[2]))
    visited = [0 for i in range(n)]
    visited[0] = 1
    min_dis = 999999
    bfs_queue = queue.Queue()
    for j in range(len(matrix[0])):
        if matrix[0][j][1] != 0:
            bfs_queue.put(matrix[0][j][0])
            min_dis = min(min_dis, matrix[0][j][1])
    while not bfs_queue.empty():
        node = bfs_queue.get()
        if visited[node] == 0:
            visited[node] = 1
            for i in range(len(matrix[node])):
                if matrix[node][i][1] != 0:
                    min_dis = min(min_dis, matrix[node][i][1])
                    if visited[matrix[node][i][0]] == 0:
                        bfs_queue.put(matrix[node][i][0])
    return min_dis
    

print(minScore(None, 4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))