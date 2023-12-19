def maxProfit(self, prices):
    sales = [0 for i in range(3)]
    buy = [float('-inf') for i in range(3)]
    for p in prices:
        for i in range(1, 3):
            buy[i] = max(buy[i], sales[i - 1] - p)
            sales[i] = max(sales[i], buy[i] + p)
    return sales[-1]

print(maxProfit(None, [1,2,4,2,5,7,2,4,9,0]))