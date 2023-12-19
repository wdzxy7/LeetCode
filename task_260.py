def singleNumber(self, nums):
    nums.sort()
    res = []
    i = 0
    while i < len(nums):
        if i + 1 == len(nums):
            res.append(nums[-1])
            return res
        if nums[i] != nums[i + 1]:
            res.append(nums[i])
            if len(res) == 2:
                return res
            if i + 2 < len(nums):
                if nums[i + 1] != nums[i + 2]:
                    return [nums[i], nums[i + 1]]
                else:
                    i += 1
                    continue
            else:
                return [nums[i], nums[i + 1]]
        i += 2


print(singleNumber(None, [0,1,1,2]))