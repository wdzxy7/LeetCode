def change(self, amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    return dp[-1]

print(change(None, 5, [1, 2, 5]))