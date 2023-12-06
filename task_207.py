def canFinish(self, numCourses, prerequisites):
    in_degree = [0 for i in range(numCourses)]
    visited = [1 for i in range(numCourses)]
    connect = [[] for i in range(numCourses)]
    for course in prerequisites:
        in_degree[course[0]] += 1
        connect[course[1]].append(course[0])
    while sum(visited) != 0:
        node = -1
        for i in range(numCourses):
            if visited[i] and in_degree[i] == 0:
                visited[i] = 0
                node = i
                break
        if node == -1:
            return False
        for i in connect[node]:
            in_degree[i] -= 1
    return True

print(canFinish(None, 2, [[1,0], [0,1]]))
