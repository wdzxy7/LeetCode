def punishmentNumber(self, n: int) -> int:
    def judge(num, now, index, base):
        t = False
        if now > base:
            return False
        if now == base and index == len(num):
            return True
        pre = now
        for j in range(index, len(num)):
            now += int(num[index: j + 1])
            t = t or judge(num, now, j + 1, base)
            if t is True:
                break
            now = pre
        return t
    res = 0
    for i in range(1, n+1):
        if judge(str(i * i), 0, 0, i):
            res += i ** 2
    return res

print(punishmentNumber(None, 37))