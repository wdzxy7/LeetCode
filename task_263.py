def isUgly(self, n):
    if n <= 0:
       return False
    factors = [2,3,5]
    for factor in factors:
        while n % factor == 0:
            n = n // factor
    return n == 1

print(isUgly(None, 1))