def kthGrammar(self, n, k):
    k_list = []
    count = 0
    t = k
    while count < n - 1:
        d = t % 2
        k_list.insert(0, d)
        t = round((t + 0.1) / 2)
        count += 1
    res = 0
    for i in k_list:
        # 右走
        if i == 0:
            if res == 0:
                res = 1
            else:
                res = 0
        # 左走
        else:
            if res == 0:
                res = 0
            else:
                res = 1
    return res


print(kthGrammar(None, 3, 1))