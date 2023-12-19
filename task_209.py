def minSubArrayLen(self, target, nums):
    if sum(nums) < target:
        return 0
    front = 0
    back = 0
    s = nums[front]
    res = float('inf')
    while back < len(nums) and front < len(nums):
        if s < target:
            if front + 1 == len(nums):
                break
            front += 1
            s += nums[front]
        else:
            res = min(res, front - back + 1)
            s -= nums[back]
            back += 1
    return res

print(minSubArrayLen(None, 11, [1,2,3,4,5]))