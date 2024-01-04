def rob(self, nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    def search(start, end, robbed , norob):
        for i in range(start + 1, end):
            t = robbed
            robbed = max(norob + nums[i], robbed)
            norob = t
        return max(robbed, norob)
    return max(search(0, len(nums) - 1, nums[0], 0), search(1, len(nums), nums[1], 0))

print(rob(None, [1,3,1,3,100]))