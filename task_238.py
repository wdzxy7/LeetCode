def productExceptSelf(self, nums):
    mul = 0
    zero = False
    zero_count = 0
    for i in nums:
        if i == 0:
            zero = True
            zero_count += 1
            continue
        else:
            if mul == 0:
                mul = 1
            mul *= i
    res = []
    for i in nums:
        if zero:
            if i == 0 and zero_count == 1:
                res.append(mul)
            else:
                res.append(0)
        else:
            res.append(mul // i)
    return res

print(productExceptSelf(None, [0, 0]))