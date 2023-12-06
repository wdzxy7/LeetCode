def kthSmallest(self, matrix, k):
    res = []
    while matrix:
        res += matrix[0]
        del matrix[0]
    res.sort()
    return res[k - 1]


print(kthSmallest(None, [[1,5,9],[10,11,13],[12,13,15]], 8))