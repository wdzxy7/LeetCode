def climbStairs(self, n):
    step = [1, 2]
    for i in range(n - 2):
        t = step[0] + step[1]
        step[0] = step[1]
        step[1] = t
    return step[-1]

print(climbStairs(None, 3))