def maxProfit(self, prices):
    sale = [[0, 0] for i in range(len(prices))]
    sale[0][1] = -prices[0]
    for i in range(1, len(prices)):
        if i == 1:
            sale[i][0] = max(sale[i - 1][0], sale[i - 1][1] + prices[i])
            sale[i][1] = max(sale[i][0] - prices[i], sale[i - 1][1])
        else:
            sale[i][0] = max(sale[i - 1][0], sale[i - 1][1] + prices[i])
            sale[i][1] = max(sale[i - 2][0] - prices[i], sale[i - 1][1])
    return max(sale[-1])

print(maxProfit(None, [1,2,3,0,2]))