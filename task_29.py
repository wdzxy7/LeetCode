def divide(self, dividend, divisor):
    neg = True
    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        neg = False
    dividend = abs(dividend)
    divisor = abs(divisor)
    if divisor > dividend:
        return 0
    star = 10
    while divisor * star < dividend:
        star = star * 10
    front = star
    end = 0
    res = star
    while front > end:
        mid = (front + end) // 2
        if divisor * mid > dividend:
            front = mid - 1
            res = front
        elif divisor * mid < dividend:
            end = mid + 1
            res = end
        else:
            res = mid
            break
    if neg:
        if res * divisor > dividend:
            return 0 - res + 1
        else:
            return 0 - res
    else:
        if res * divisor > dividend:
            return res - 1
        else:
            return res


print(divide(None, -2147483648, -1))