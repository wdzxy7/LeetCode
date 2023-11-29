def digitSum(self, s, k):
    s = list(s)
    s = [int(i) for i in s]
    while len(s) > k:
        t_list = []
        i = 0
        while i < len(s):
            t_list.append(sum(s[i:i+k]))
            i += k
        temp = ''
        for i in t_list:
            temp += str(i)
        s = list(temp)
        s = [int(i) for i in s]
    res = ''
    for i in s:
        res += str(i)
    return res


print(digitSum(None, "01234567890", 2))