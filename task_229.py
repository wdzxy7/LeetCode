def majorityElement(self, nums):
    nums.sort()
    length = len(nums)
    pre = nums[0]
    count = 1
    res = []
    thread = length // 3
    for i in range(1, length):
        if pre != nums[i]:
            if count > thread:
                res.append(pre)
            count = 0
        pre = nums[i]
        count += 1
    if count > thread:
        res.append(pre)
    return res

print(majorityElement(None, [3,2,3]))