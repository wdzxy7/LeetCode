def numRollsToTarget(self, n, k, target):
    MOD = 10 ** 9 + 7
    dp = [0 for i in range(target + 1)]
    up_dp = [0 for i in range(target + 1)]
    for i in range(1, min(k + 1, target + 1)):
        dp[i] = 1
    for i in range(1, n):
        for j in range(i + 1, min(k * (i + 1) + 1, target + 1)):
            for num in range(1, k + 1):
                if j - num <= 0:
                    break
                up_dp[j] += dp[j - num]
        dp = up_dp.copy()
        up_dp = [0 for i in range(target + 1)]
    return dp[target] % MOD


print(numRollsToTarget(None, 1, 6,3))