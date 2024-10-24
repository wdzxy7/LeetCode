def maxSumDivThree(self, nums):
    f = [0, -float("inf"), -float("inf")]
    for num in nums:
        g = f[:]
        for i in range(3):
            g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
        f = g
    return f[0]

print(maxSumDivThree(None, [8,6,7,1,0]))
