def intToRoman(num):
    res = ''
    while num > 0:
        if num >= 1000:
            t = num // 1000
            for i in range(t):
                res += 'M'
            num = num % 1000
        elif num >= 100:
            t = num // 100
            if t != 4 and t != 9 and t < 5:
                for i in range(t):
                    res += 'C'
            elif t == 4:
                res += 'CD'
            elif t == 9:
                res += 'CM'
            else:
                res += 'D'
                for i in range(t - 5):
                    res += 'C'
            num = num % 100
        elif num >= 10:
            t = num // 10
            if t != 4 and t != 9 and t < 5:
                for i in range(t):
                    res += 'X'
            elif t == 4:
                res += 'XL'
            elif t == 9:
                res += 'XC'
            else:
                res += 'L'
                for i in range(t - 5):
                    res += 'X'
            num = num % 10
        else:
            t = num
            if t != 4 and t != 9 and t < 5:
                for i in range(t):
                    res += 'I'
            elif t == 4:
                res += 'IV'
            elif t == 9:
                res += 'IX'
            else:
                res += 'V'
                for i in range(t - 5):
                    res += 'I'
            return res
    return res
print(intToRoman(10))