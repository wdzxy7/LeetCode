def maxAbsoluteSum(self, nums):
    max_sum, max_res = 0, 0
    min_sum, min_res = 0, 0
    for i in nums:
        max_sum += i
        max_res = max(max_sum, max_res)
        max_sum = max(0, max_sum)

        min_sum += i
        min_res = min(min_sum, min_res)
        min_sum = min(0, min_sum)
    return max(max_res, abs(min_res))

print(maxAbsoluteSum(None, [2,-5,1,-4,3,-2]))