def combinationSum3(self, k, n):
    res_list = []
    def search(t_res, num, length):
        if length == k and sum(t_res) == n:
            res_list.append(t_res.copy())
            return
        elif length > k:
            return
        else:
            for i in range(num, 10):
                t_res.append(i)
                search(t_res, i + 1, length + 1)
                del t_res[-1]
    search([], 1, 0)
    return res_list

print(combinationSum3(None, 4, 1))