def combinationSum4(self, nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        s = 0
        for j in nums:
            if i - j >= 0:
                s += dp[i - j]
        dp[i] = s
    return dp[-1]


print(combinationSum4(None, [1,2,3], 4))