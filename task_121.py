def maxProfit(prices):
    min_price = prices[0]
    max_sale = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if prices[i] - min_price > max_sale:
                max_sale = prices[i] - min_price
    return max_sale