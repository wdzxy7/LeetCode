def threeSumClosest(self, nums, target):
    nums = sorted(nums)
    l = len(nums)
    if l == 3:
        return sum(nums)
    min_diff = 999
    min_sum = 999
    for i in range(0, l):
        front = i + 1
        back = l - 1
        while front < back:
            s = nums[i] + nums[front] + nums[back]
            if s == target:
                return s
            elif s > target:
                diff = s - target
                back -= 1
            else:
                diff = target - s
                front += 1
            if diff < min_diff:
                min_diff = diff
                min_sum = s
    return min_sum


print(threeSumClosest(None, [4,0,5,-5,3,3,0,-4,-5], -2))