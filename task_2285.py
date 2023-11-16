def maximumImportance(self, n, roads):
    array = [0 for i in range(n)]
    for v, d in roads:
        array[v] += 1
        array[d] += 1
    array.sort()
    return sum(array[i] * (i + 1) for i in range(n))


print(maximumImportance(None, 5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))