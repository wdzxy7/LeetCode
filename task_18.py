def fourSum(self, nums, target):
    nums = sorted(nums)
    front = 0
    l = len(nums) - 1
    res_set = []
    while front <= l - 3:
        back = l
        while back >= front + 3:
            t_front = front + 1
            t_back = back - 1
            while t_front < t_back:
                if nums[front] + nums[t_front] + nums[t_back] + nums[back] == target:
                    res_set.append((nums[front], nums[t_front], nums[t_back], nums[back]))
                    t = t_front + 1
                    while nums[t] == nums[t_front] and t < t_back:
                        t += 1
                    t_front = t
                    t = t_back - 1
                    while nums[t] == nums[t_back] and t > t_front:
                        t -= 1
                    t_back = t
                elif nums[front] + nums[t_front] + nums[t_back] + nums[back] > target:
                    t_back -= 1
                else:
                    t_front += 1
            back -= 1
        front += 1
    return list(list(i) for i in set(res_set))

print(fourSum(None, [1,0,-1,0,-2,2], 0))