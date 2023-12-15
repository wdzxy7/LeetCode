def combine(self, n, k):
    res_list = []
    def search(deep, t_res, t_num):
        if deep == k:
            res_list.append(t_res.copy())
            return
        else:
            for i in range(t_num, n + 1):
                t_res.append(i)
                search(deep + 1, t_res, i + 1)
                del t_res[-1]
    search(0, [], 1)
    return res_list

print(combine(None, 4, 2))
