def minMoves2(self, nums):
    nums.sort()
    mid = len(nums) // 2
    mid = nums[mid]
    res = 0
    for i in nums:
        res += abs(i - mid)
    return res


print(minMoves2(None, [1,0,0,8,6]))
