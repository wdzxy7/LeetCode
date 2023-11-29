def maxProfit(self, prices, fee):
    bp = [[0, -prices[0]] for i in range(len(prices))]
    for i in range(1, len(prices)):
        bp[i][0] = max(bp[i - 1][0], bp[i - 1][1] + prices[i] - fee)
        bp[i][1] = max(bp[i - 1][0] - prices[i], bp[i - 1][1])
    return max(bp[len(prices) - 1])

print(maxProfit(None, [1,4,6,2,8,3,10,14], 3))