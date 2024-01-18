def minMoves(self, nums):
    min_num = min(nums)
    res = 0
    for i in nums:
        res += i - min_num
    return res


print(minMoves(None, [1,2,3]))