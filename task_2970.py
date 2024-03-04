def incremovableSubarrayCount(self, nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums) + 1):
            sub_arr = nums[:i] + nums[j:]
            if sub_arr == sorted(set(sub_arr)):
                res += 1
    return res

print(incremovableSubarrayCount(None, [6,5,7,8]))