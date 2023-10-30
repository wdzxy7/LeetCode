def searchRange(self, nums, target):
    front = 0
    back = len(nums) - 1
    sign = False
    if front == back and nums[0] == target:
        return [0, 0]
    while front <= back:
        mid = (front + back) // 2
        if nums[mid] < target:
            front = mid + 1
        elif nums[mid] > target:
            back = mid - 1
        else:
            sign = True
            back = mid
            front = mid
            break
    while front > 0 and nums[front - 1] == target:
        front -= 1
    while back < len(nums) - 1 and nums[back + 1] == target:
        back += 1
    if sign:
        return [front, back]
    else:
        return [-1,-1]


print(searchRange(None, [1, 5], 5))