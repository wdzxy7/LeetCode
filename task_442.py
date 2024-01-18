def findDuplicates(self, nums):
    nums.sort()
    res = []
    pre = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == pre:
            res.append(pre)
        else:
            pre = nums[i]
    return res

print(findDuplicates(None, [4,3,2,7,8,2,3,1]))