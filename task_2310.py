def minimumNumbers(self, num, k):
    sub = num % 10
    if num == 0:
        return 0
    for i in range(1, 11):
        if (k * i) % 10 == sub and k * i <= num:
            return i
    return -1


print(minimumNumbers(None, 10, 1))