def largestDivisibleSubset(self, nums):
    nums = sorted(nums)
    index = []
    max_len = []
    for i in range(len(nums)):
        sign = True
        max_sert_len = -1
        for j in range(i - 1, -1, -1):
            if nums[i] % nums[j] == 0:
                if max_len[j] > max_sert_len:
                    t_len = max_len[j]
                    t_index = j
                    max_sert_len = t_len
                sign = False
        if sign:
            max_len.append(1)
            index.append(-1)
        else:
            max_len.append(t_len + 1)
            index.append(t_index)
    max_index = max_len.index(max(max_len))
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = index[max_index]
    res.reverse()
    return res


print(largestDivisibleSubset(None, [4,8,10,240]))