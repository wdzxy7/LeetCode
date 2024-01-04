from functools import cache


def coinChange2(self, coins, amount):
    coins.sort(reverse=True)
    if amount == 0:
        return 0
    min_count = float('inf')
    @cache
    def search(res_amount, index, count):
        nonlocal min_count
        if count > min_count or res_amount < 0:
            return
        if res_amount == 0:
            if count < min_count:
                min_count = count
            return
        for i in range(index, len(coins)):
            count += 1
            search(res_amount - coins[i], i, count)
            count -= 1
    search(amount, 0, 0)
    if min_count == float('inf'):
        min_count = -1
    return min_count

def coinChange(self, coins, amount):
    if amount == 0:
        return 0
    dp = [float('inf') for i in range(amount + 1)]
    dp[0] = 0
    for i in range(1, amount + 1):
        min_coin = float('inf')
        for coin in coins:
            index = i - coin
            if index < 0:
                continue
            else:
                min_coin = min(min_coin, dp[index])
        dp[i] = 1 + min_coin
    return dp[-1] if dp[-1] != float('inf') else -1

print(coinChange(None, [1,2,5], 11))