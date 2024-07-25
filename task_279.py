def numSquares(self, n):
    dp = [float('inf') for i in range(n + 1)]
    dp[0] = 0
    real_num = []
    for i in range(1, 10001):
        if i ** 0.5 == round(i ** 0.5):
            real_num.append(i)
    for num in real_num:
        for i in range(1, n + 1):
            if i - num >= 0:
                dp[i] = min(dp[i], dp[i - num] + 1)
    return dp[-1]


print(numSquares(None, 121))