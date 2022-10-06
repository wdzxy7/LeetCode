def myPow(x, n):
    result = x
    ls = []
    sign = False
    if n < 0:
        sign = True
    n = abs(n)
    if n == 0:
        return 1
    while n != 1 and n != 0:
        ls.append(n % 2)
        n = n // 2
    for i in range(len(ls) - 1, -1, -1):
        result *= result
        if ls[i] == 1:
            result *= x
    if sign:
        result = 1 / result
    result = round(result, 5)
    return result


res = myPow(0.44528, 0)
print(res)
