import heapq
import queue


def maxProfit2(self, k, prices):
    dp = [[0, 0] for i in range(len(prices))]
    dp[0][1] = -prices[0]
    buy_price = prices[0]
    buy_day = 0
    sale_queue = queue.Queue()
    for i in range(1, len(prices)):
        # sale
        if dp[i - 1][0] < dp[i - 1][1] + prices[i]:
            sale_day = i
            sale_queue.put([prices[i] - buy_price, buy_day, sale_day, buy_price, prices[i]])
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # buy
        if dp[i][0] - prices[i] >= dp[i - 1][1]:
            buy_price = prices[i]
            buy_day = i
        dp[i][1] = max(dp[i][0] - prices[i], dp[i - 1][1])
    pre = None
    res = []
    sale = None
    # merge
    while not sale_queue.empty():
        if pre is None:
            pre = sale_queue.get()
            continue
        sale = sale_queue.get()
        if pre[2] == sale[1]:
            pre = [pre[0] + sale[0], pre[1], sale[2], pre[3], sale[4]]
        else:
            pre[0] = 0 - pre[0]
            heapq.heappush(res, pre)
            pre = sale
    if sale is not None:
        if pre[2] == sale[2]:
            pre[0] = 0 - pre[0]
            heapq.heappush(res, pre)
        else:
            sale[0] = 0 - sale[0]
            heapq.heappush(res, sale)
    elif pre is not None:
        pre[0] = 0 - pre[0]
        heapq.heappush(res, pre)
    sales = 0
    for i in range(min(k, len(res))):
        t = heapq.heappop(res)
        sales += 0 - t[0]
    return sales

def maxProfit(self, k, prices):
    sales = [0 for i in range(k + 1)]
    buy = [float('-inf') for i in range(k + 1)]
    for p in prices:
        for i in range(1, k + 1):
            buy[i] = max(buy[i], sales[i - 1] - p)
            sales[i] = max(sales[i], buy[i] + p)
    return sales[-1]


print(maxProfit(None, 2, [1,2,4,2,5,7,2,4,9,0]))