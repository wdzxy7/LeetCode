import re


def numDecodings1(self, s):
    if s[0] == '0':
        return 0
    s = re.sub(r'\d0', '*0', s)
    s_list = s.split('*0')
    count = 0
    for s in s_list:
        t_count = 1
        pre = 1
        if s == '' or s[0] == '0':
            continue
        for i in range(1, len(s)):
            if s[i - 1] != '0' and s[i - 1] < '3':
                t = t_count + pre
                pre = t_count
                t_count = t
            else:
                pre = t_count
        count += t_count
    return count

def numDecodings(self, s):
    if s[0] == '0':
        return 0
    elif '00' in s:
        return 0
    count = 1
    pre = 1
    for i in range(1, len(s)):
        if s[i] == 0:
            t = pre
            pre = count
            count = t
        elif s[i-1: i + 1] > '26':
            pre = count
        elif s[i - 1] != '0' and s[i - 1] < '3':
            t = count + pre
            pre = count
            count = t
        else:
            pre = count
    return count


print(numDecodings(None, '1101'))