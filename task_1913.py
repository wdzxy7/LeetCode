def maxProductDifference(self, nums):
    nums.sort(reverse=True)
    return nums[0] * nums[1] - nums[-2] * nums[-1]

print(maxProductDifference(None, [5,6,2,7,4]))