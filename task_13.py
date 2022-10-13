def romanToInt(self, s):
    s = list(s)
    quick_dict = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'V': 5,
                  'I': 1

    }
    res = 0
    i = 0
    while i < len(s):
        try:
            if s[i] == 'I' and s[i + 1] == 'V':
                res += 4
                i += 1
            elif s[i] == 'I' and s[i + 1] == 'X':
                res += 9
                i += 1
            elif s[i] == 'X' and s[i + 1] == 'L':
                res += 40
                i += 1
            elif s[i] == 'X' and s[i + 1] == 'C':
                res += 90
                i += 1
            elif s[i] == 'C' and s[i + 1] == 'D':
                res += 400
                i += 1
            elif s[i] == 'C' and s[i + 1] == 'M':
                res += 900
                i += 1
            else:
                res += quick_dict[s[i]]
        except:
            res += quick_dict[s[i]]
        i += 1
    return res

print(romanToInt(None, "III"))