def myAtoi(self, s):
    number_dict = {}
    for i in range(0, 11):
        number_dict[str(i)] = i
    keys = number_dict.keys()
    s = list(s)
    sign = False
    res = 0
    num_sign = False
    space_sign = True
    for i in range(len(s)):
        if s[i] in keys:
           res = res * 10 + number_dict[s[i]]
           num_sign = True
           space_sign = False
           continue
        if num_sign is False:
            if s[i] == '-':
                try:
                    if s[i + 1] in keys:
                        sign = True
                        continue
                    else:
                        break
                except:
                    break
            elif s[i] == '+':
                try:
                    if s[i + 1] in keys:
                        continue
                    else:
                        break
                except:
                    break
        if s[i] == ' ' and space_sign:
            continue
        else:
            break
    if res >= 2147483648 and sign:
        res = 0 - 2147483648
    elif res >= 2147483648 and sign is False:
        res = 2147483648
    elif sign:
        return 0 - res
    return res


print(myAtoi(None, '   +42'))