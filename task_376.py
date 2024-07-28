def wiggleMaxLength(self, nums):
    dp = [[0, 0] for i in range(len(nums))]
    dp[0] = [1, 1]
    for i in range(1, len(nums)):
        if nums[i] > nums[i -1]:
            dp[i][0] = max(dp[i-1][1] + 1, dp[i-1][0])
            dp[i][1] = dp[i-1][1]
        elif nums[i] < nums[i-1]:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i - 1][0] + 1, dp[i-1][1])
        else:
            dp[i][1] = dp[i-1][1]
            dp[i][0] = dp[i-1][0]
    return max(dp[-1][1], dp[-1][0])


print(wiggleMaxLength(None, [1,17,5,10,13,15,10,5,16,8]))