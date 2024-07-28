def maxDotProduct(self, nums1, nums2):
    dp = [[0 for i in range(len(nums1))] for i in range(len(nums2))]
    dp[0][0] = nums1[0] * nums2[0]
    for i in range(1, len(nums1)):
        dp[0][i] = max(dp[0][i - 1], nums2[0] * nums1[i])
    for j in range(1, len(nums2)):
        dp[j][0] = max(dp[j - 1][0], nums1[0] * nums2[j])
    for i in range(1, len(nums2)):
        for j in range(1, len(nums1)):
            dp[i][j] = max(dp[i - 1][j - 1] + nums2[i] * nums1[j], dp[i][j - 1], nums2[i] * nums1[j], dp[i - 1][j])
    return dp[-1][-1]


print(maxDotProduct(None, [5,-4,-3], [-4,-3,0,-4,2]))