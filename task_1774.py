def closestCost(self, baseCosts, toppingCosts, target):
    if min(baseCosts) > target:
        return min(baseCosts)
    cans = [False] * (target + 1)
    cans[0] = True
    res = float('inf')
    for base in baseCosts:
        if base > target:
            res = min(res, base)
        else:
            cans[base] = True
    for topping in toppingCosts:
        for i in range(2):
            for j in range(target, 0, -1):
                if cans[j] and j + topping > target:
                    res = min(res, j + topping)
                elif not cans[j] and j - topping > 0:
                    cans[j] = cans[j] or cans[j - topping]
    for i in range(target, 0, -1):
        if cans[i]:
            if target - i < res - target:
                return i
            else:
                res
    return res


print(closestCost(None, [4], [9], 9))