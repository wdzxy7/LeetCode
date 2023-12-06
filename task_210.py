def findOrder(self, numCourses, prerequisites):
    in_degree = [0 for i in range(numCourses)]
    visited = [1 for i in range(numCourses)]
    connect = [[] for i in range(numCourses)]
    for course in prerequisites:
        in_degree[course[0]] += 1
        connect[course[1]].append(course[0])
    study = []
    while sum(visited) != 0:
        node = -1
        for i in range(numCourses):
            if visited[i] and in_degree[i] == 0:
                visited[i] = 0
                node = i
                study.append(node)
                break
        if node == -1:
            return []
        for i in connect[node]:
            in_degree[i] -= 1
    return study

print(findOrder(None, 4, [[1,0],[2,0],[3,1],[3,2]]))
