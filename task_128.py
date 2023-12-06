def longestConsecutive(self, nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    count = 0
    pre = nums[0] - 1
    max_len = 0
    for i in range(len(nums)):
        if nums[i] == pre + 1:
            count += 1
        elif nums[i] == pre:
            continue
        else:
            if count >= max_len:
                max_len = count
            count = 1
        pre = nums[i]
    if count > max_len:
        max_len = count
    return max_len



print(longestConsecutive(None,[7,-9,3,-6,3,5,3,6,-2,-5,8,6,-4,-6,-4,-4,5,-9,2,7,0,0]))