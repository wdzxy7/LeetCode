def minimizeTheDifference(self, mat, target):
    m, n = len(mat), len(mat[0])
    f = {0}
    for i in range(m):
        g = set()
        for x in mat[i]:
            for j in f:
                g.add(j + x)
        f = g

    ans = float("inf")
    for x in f:
        ans = min(ans, abs(x - target))
    return ans

print(minimizeTheDifference(None, [[1,2,3],[4,5,6],[7,8,9]], 13))