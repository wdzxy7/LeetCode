def removeDigit(self, number, digit):
    res = []
    for i in range(len(number)):
        if number[i] == digit:
            res.append(number[:i] + number[i+1:])
    return max(res)

print(removeDigit(None, '551', '5'))