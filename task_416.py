def canPartition(self, nums):
    if sum(nums) % 2 != 0 or len(nums) < 2 != 0:
        return False
    half = sum(nums) // 2
    nums.sort()
    dp = [False] * (half + 1)
    dp[0] = True
    for i, num in enumerate(nums):
        for j in range(half, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[-1]


print(canPartition(None, [1,2,5]))