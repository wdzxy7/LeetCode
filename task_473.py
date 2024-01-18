def makesquare(self, matchsticks):
    if sum(matchsticks) % 4:
        return False
    d = sum(matchsticks) // 4
    matchsticks.sort(reverse=True)
    edge = [0, 0, 0, 0]
    def search(index):
        nonlocal edge
        if index == len(matchsticks):
            return True
        for i in range(4):
            edge[i] += matchsticks[index]
            if edge[i] <= d and search(index + 1):
                return True
            edge[i] -= matchsticks[index]
        return False
    return search(0)


print(makesquare(None, [5,5,5,5,4,4,4,4,3,3,3,3]))