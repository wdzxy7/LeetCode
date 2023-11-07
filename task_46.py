def permute(self, nums):
    res = []
    def search(res_list, num_list, temp):
        if num_list[0] == num_list[-1]:
            res_list.append(temp + [num_list[0]])
            return
        else:
            for num in num_list:
                t = num_list.copy()
                t.remove(num)
                search(res_list, t, temp + [num])
    search(res, nums, [])
    return res


print(permute(None, [1]))