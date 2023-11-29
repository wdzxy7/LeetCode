def separateDigits(self, nums):
    res = []
    for num in nums:
        res += list(str(num))
    return [int(i) for i in res]

print(separateDigits(None, [13,25,83,77]))