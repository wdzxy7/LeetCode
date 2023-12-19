def rob(self, nums):
    if len(nums) < 3:
        return max(nums)
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]
    for i in range(3, len(nums)):
        dp[i] = nums[i] + max(dp[i - 3], dp[i - 2])
    return max(dp[-1], dp[-2])

print(rob(None, [2,7,9,3,1]))