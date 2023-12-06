import math


def minimumFuelCost1(self, roads, seats):
    def search():
        for i in range(node_len):
            if visited[i] == 0 and degree[i] == 0.5:
                return i
        return -1
    node_len = len(roads) + 1
    visited = [0 for i in range(node_len)]
    visited[0] = 1
    degree = [0 for i in range(node_len)]
    node_people = [1 for i in range(node_len)]
    node_people[0] = 0
    node_connect = [[] for i in range(node_len)]
    for road in roads:
        degree[road[0]] += 0.5
        degree[road[1]] += 0.5
        node_connect[road[0]].append(road[1])
        node_connect[road[1]].append(road[0])
    gas = 0
    while True:
        zero_node = search()
        if zero_node == -1:
            break
        visited[zero_node] = 1
        node_nei = node_connect[zero_node]
        for node in node_nei:
            if visited[node] and node != 0:
                continue
            degree[node] -= 0.5
            node_people[node] += node_people[zero_node]
            gas += math.ceil(node_people[zero_node] / seats)
    return gas


def minimumFuelCost(self, roads, seats):
    node_len = len(roads) + 1
    node_connect = [[] for i in range(node_len)]
    for road in roads:
        node_connect[road[0]].append(road[1])
        node_connect[road[1]].append(road[0])
    gas = 0
    def dfs(node, pre):
        nonlocal gas
        all_people = 1
        for nei in node_connect[node]:
            if nei == pre:
                continue
            nei_people = dfs(nei, node)
            all_people += nei_people
            gas += math.ceil((nei_people) / seats)
        return all_people
    dfs(0, -1)
    return gas

print(minimumFuelCost(None, [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2))