def deleteAndEarn(self, nums):
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    dp = [0, nums[0]]
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            dp[1] += nums[i]
        else:
            break
        i += 1
    while i < len(nums):
        if nums[i] > nums[i-1] + 1:
            dp.append(max(dp) + nums[i])
        elif nums[i] == nums[i-1] + 1:
            dp.append(max(dp[:-1]) + nums[i])
        else:
            dp[-1] += nums[i]
        i += 1
    return max(dp)

print(deleteAndEarn(None, [8,10,4,9,1,3,5,9,4,10]))