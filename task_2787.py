def numberOfWays(self, n, x):
    MOD = 10 ** 9 + 7
    m = round(n ** (1/x))
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n, i ** x - 1, -1):
            dp[j] = dp[j - i ** x] + dp[j]
    return dp[-1] % MOD

print(numberOfWays(None, 4, 1))