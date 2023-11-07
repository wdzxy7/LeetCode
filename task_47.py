def permute(self, nums):
    res = []
    def search(res_list, num_list, temp):
        if len(num_list) == 1:
            res_list.append(tuple(temp + [num_list[0]]))
            return
        else:
            for num in num_list:
                t = num_list.copy()
                t.remove(num)
                search(res_list, t, temp + [num])
    search(res, nums, [])
    res = set(res)
    return [list(i) for i in res]


print(permute(None, [1,1,2]))