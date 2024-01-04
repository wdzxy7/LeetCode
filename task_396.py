def maxRotateFunction(self, nums):
    pre = 0
    length = len(nums)
    for i in range(length):
        pre += nums[i] * i
    s = sum(nums)
    res_max = pre
    for i in range(1, length):
        res = pre + s - length * nums[length - i]
        res_max = max(res, res_max)
        pre = res
    return res_max


print(maxRotateFunction(None, [1,2,3,4,5,6,7,8,9,10]))