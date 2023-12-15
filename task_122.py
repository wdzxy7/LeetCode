def maxProfit(self, prices):
    dp = [[0, -prices[0]] for i in range(len(prices))]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i][0] - prices[i], dp[i - 1][1])
    return max(dp[-1])

print(maxProfit(None, [7,1,5,3,6,4]))