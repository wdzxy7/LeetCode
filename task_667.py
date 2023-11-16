def constructArray(self, n, k):
    if (k + 2) // 2 != k / 2:
        mid = (k + 2) // 2 + 1
    else:
        mid = k / 2
    change = [i for i in range(1, mid)]
    sert = [i for i in range(mid, k + 2)]
    keep = [i for i in range(k + 2, n + 1)]
    sert_index = 1
    l2 = len(sert) - 1
    while l2 >= 0:
        change.insert(sert_index, sert[l2])
        l2 -= 1
        sert_index += 2
    return change + keep

print(constructArray(None, 3, 2))