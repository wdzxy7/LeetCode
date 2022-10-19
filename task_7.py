def reverse(self, x):
    sign = False
    if x < 0:
        sign = True
        x = 0 - x
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    if res > 4294967296:
        return 0
    if sign:
        return 0 - res
    return res

print(reverse(None, -123))