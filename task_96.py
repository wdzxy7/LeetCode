def numTrees(self, n):
    trees = [0 for i in range(n + 1)]
    trees[0] = 1
    trees[1] = 1
    trees[2] = 2
    if n < 3:
        return trees[n]
    for i in range(3, n + 1):
        for j in range(0, i):
            trees[i] += trees[j] * trees[i - j - 1]
    return trees[-1]

print(numTrees(None, 3))