def countPaths(self, n, roads):
    degree = [0] * n
    edges = {}
    min_dis = [0] * n
    for road in roads:
        degree[road[0]] += 1
        degree[road[1]] += 1
        try:
            edges[road[0]].append([road[1], road[-1]])
        except:
            edges[road[0]] = [[road[1], road[-1]]]
        try:
            edges[road[1]].append([road[0], road[-1]])
        except:
            edges[road[1]] = [[road[0], road[-1]]]
    degree[-1] = -1
    root = n - 1
    connect = edges[6]
    while True:
        for node in connect:
            degree[node[0]] -= 1
            if min_dis[node[0]] != 0:
                min_dis[node[0]] = min(min_dis[node[0]], min_dis[root] + node[1])
            else:
                min_dis[node[0]] = node[1]
        root = degree.index(0)
        degree[root] = -1
        connect = edges[root]
    return None

print(countPaths(None, 7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))