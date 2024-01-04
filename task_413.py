def numberOfArithmeticSlices(self, nums):
    dp = [0] * len(nums)
    if len(nums) <= 2:
        return 0
    pre_diff = nums[1] - nums[0]
    count = 2
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff != pre_diff:
            count = 2
            pre_diff = diff
            continue
        count += 1
        dp[i] = count - 2
    return sum(dp)

print(numberOfArithmeticSlices(None, [1, 2, 3, 4, 7, 8, 9]))