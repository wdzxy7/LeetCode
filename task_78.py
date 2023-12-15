def subsets(self, nums):
    res_list = [[]]
    def search(t_res, index):
        for i in range(index, len(nums)):
            t_res.append(nums[i])
            res_list.append(t_res.copy())
            search(t_res, i + 1)
            del t_res[-1]
    search([], 0)
    return res_list


print(subsets(None, [0]))