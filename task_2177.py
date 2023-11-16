def sumOfThree(self, num):
    mid = num // 3
    if mid * 3 == num:
        return [mid - 1, mid, mid + 1]
    return []

print(sumOfThree(None, 9))