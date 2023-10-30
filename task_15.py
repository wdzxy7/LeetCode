def threeSum(self, nums):
    nums = sorted(nums)
    print(nums)
    l = len(nums)
    if l == 3 and (nums[0] + nums[1] + nums[2] == 0):
        return [nums]
    res = []
    for i in range(0, l):
        front = i + 1
        back = l - 1
        while front < back:
            if nums[i] + nums[front] + nums[back] == 0:
                if [nums[i], nums[front], nums[back]] not in res:
                    res.append([nums[i], nums[front], nums[back]])
                front += 1
            elif nums[i] + nums[front] + nums[back] < 0:
                front += 1
            else:
                back -= 1
    return res


print(threeSum(None, [1,-1,0, 0]))