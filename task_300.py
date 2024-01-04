def lengthOfLIS(self, nums):
    dp = [1 for i in range(len(nums))]
    t_max = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] and dp[i - 1] >= t_max:
            dp[i] += dp[i - 1]
            t_max = dp[i]
        else:
            max_l = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    max_l = max(max_l, dp[j])
            dp[i] += max_l
            t_max = max(dp[i], t_max)
    return max(dp)


print(lengthOfLIS(None, [1,3,6,7,9,4,10,5,6]))