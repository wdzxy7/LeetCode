def findTargetSumWays(self, nums, target):
    s = sum(nums) - abs(target)
    if s < 0 or s % 2:
        return 0
    m = s // 2  # 背包容量
    f = [1] + [0] * m
    for x in nums:
        for c in range(m, x - 1, -1):
            f[c] += f[c - x]
    return f[m]


print(findTargetSumWays(None, [1,1,1,1,1], 3))