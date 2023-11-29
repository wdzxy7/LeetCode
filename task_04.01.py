def findWhetherExistsPath(self, n, graph, start, target):
    connect_list = [set() for i in range(n)]
    for con in graph:
        connect_list[con[0]].add(con[1])
    connect_list = [list(i) for i in connect_list]
    dfs_stack = connect_list[start]
    visit = [0 for i in range(n)]
    while dfs_stack:
        node = dfs_stack.pop()
        if node == target:
            return True
        if visit[node] == 0:
            visit[node] = 1
            dfs_stack += connect_list[node]
    return False


print(findWhetherExistsPath(None, 5, [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], 0, 5))