def countGoodStrings(self, low, high, zero, one):
    MOD = 10**9+7
    res = [0 for i in range(high + 1)]
    res[zero] += 1
    res[one] += 1
    for i in range(min(zero, one) + 1, high + 1):
        res[i] += res[i - zero]
        res[i] += res[i - one]
    return sum(res[low:high + 1]) % MOD
# 00 01 10 11
print(countGoodStrings(None, 3,3,1,1))