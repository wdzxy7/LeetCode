def maxSubArray(self, nums):
    pre = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        pre = max(nums[i] + pre, nums[i])
        if pre > max_sum:
            max_sum = pre
    return max_sum

print(maxSubArray(None, [-2,1,-3,4,-1,2,1,-5,4]))