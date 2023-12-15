def maxSubarraySumCircular(self, nums):
    nums = nums * 2
    del nums[-1]
    t_max = nums[0]
    front_sum = nums[0]
    for i in range(1, len(nums)):
        if front_sum + nums[i] < nums[i]:
            front_sum = nums[i]
        else:
            front_sum = front_sum + nums[i]
        if front_sum > t_max:
            t_max = front_sum
    return t_max

print(maxSubarraySumCircular(None, [5,-3,5]))