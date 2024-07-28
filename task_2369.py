def validPartition(self, nums):
    dp = [False] * (len(nums) + 1)
    dp[0] = True
    for i in range(1, len(nums) + 1):
        if i >= 2:
            dp[i] = dp[i - 2] and (nums[i - 1] == nums[i - 2])
        if i >= 3:
            dp[i] = dp[i] or (dp[i - 3] and ((nums[i - 1] == nums[i - 2] == nums[i - 3]) or
                                             nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2))
    return dp[-1]

print(validPartition(None, [1,1,1,2,3]))