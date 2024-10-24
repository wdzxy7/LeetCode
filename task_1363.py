def largestMultipleOfThree(self, digits):
    if sum(digits) == 0:
        return 0
    digits.sort(reverse=True)
    f = [0, float('-inf'), float('-inf')]
    chars = ['', '', '']
    for num in digits:
        g = f[:]
        for i in range(3):
            g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            if g[(i + num % 3) % 3] > f[(i + num % 3) % 3] or num == 0:
                chars[(i + num % 3) % 3] = chars[i] + str(num)
        f = g
    return chars[0]

print(largestMultipleOfThree(None, [1,1,1,2]))