from collections import Counter


def maximumTotalDamage(self, nums):
    cnt = Counter(nums)
    a = sorted(cnt.keys())
    f = [0] * (len(a) + 1)
    j = 0
    for i, x in enumerate(a):
        while a[j] < x - 2:
            j += 1
        f[i + 1] = max(f[i], f[j] + x * cnt[x])
    return f[-1]


print(maximumTotalDamage(None, [i for i in range(1000)]))