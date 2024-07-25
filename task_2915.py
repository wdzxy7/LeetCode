def lengthOfLongestSubsequence(self, nums, target):
    dp = [-1 for i in range(target + 1)]
    dp[0] = 0
    for i in nums:
        for j in range(target, i - 1, -1):
            if dp[j - i] != -1:
                dp[j] = max(dp[j], dp[j - i] + 1)
    return dp[-1]

print(lengthOfLongestSubsequence(None, [1,2,3,4,5], 7))