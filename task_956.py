
def tallestBillboard(self, rods) -> int:
    dp = {0: 0}
    for i in rods:
        for k, b in list(dp.items()):
            dp[k + i] = max(dp.get(k + i, 0), b + i)
            dp[k - i] = max(dp.get(k - i, 0), b)
    return dp[0]


print(tallestBillboard(None, [96,112,101,100,104,93,106,99,114,81,94]))