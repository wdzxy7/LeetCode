def profitableSchemes1(self, n, minProfit, group, profit):
    if minProfit == 0:
        l = len(group)
        s = 1
        while l > 0:
            s *= l
            l -= 1
        return s
    count = 0
    mod = 10**9 + 7
    work_list = []
    for need, salary in zip(group, profit):
        add_list = []
        for work in work_list:
            if work[0] >= need:
                if work[0] - need != 0:
                    add_list.append([work[0] - need, work[1] + salary])
                count += 1
        work_list += add_list
        if n >= need:
            work_list.append([n - need, salary])
            if salary >= minProfit:
                count += 1
    return count % mod

def profitableSchemes(self, n, minProfit, group, profit):
    mod = 10 ** 9 + 7
    dp = [[0 for i in range(minProfit + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for need, salary in zip(group, profit):
        for j in range(n, need - 1, -1):
            for i in range(minProfit, -1, -1):
                dp[j][i] = (dp[j][i] + dp[j - need][max(0, i - salary)]) % mod
    return dp[n][minProfit]

print(profitableSchemes(None, 64, 0, [80,40],[88,88]))