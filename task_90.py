def subsetsWithDup(self, nums):
    res = [[]]
    nums.sort()
    length = len(nums)
    def search(index, t_res):
        if index == length:
            return
        else:
            for i in range(index, length):
                t_res.append(nums[i])
                if t_res not in res:
                    res.append(t_res.copy())
                search(i + 1, t_res.copy())
                t_res.pop()
    search(0, [])
    return res

print(subsetsWithDup(None, [4,4,4,1,4]))