def search(self, nums, target):
    l = len(nums)
    if l == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    i = 0
    while i <= l - 2:
        if nums[i] < nums[i + 1]:
            i += 1
        else:
            break
    if target == nums[i]:
        return i
    else:
        if i == l - 1:
            front = 0
            back = i
        elif nums[0] <= target:
            front = 0
            back = i
        else:
            front = i + 1
            back = l - 1
    while front <= back:
        mid = (front + back) // 2
        if nums[mid] < target:
            front = mid + 1
        elif nums[mid] > target:
            back = mid - 1
        else:
            return mid
    return -1


print(search(None, [3,5,1], 3))