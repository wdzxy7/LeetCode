def removeElement(self, nums, val):
    front_ind = 0
    i = 0
    k = 0
    while i < len(nums):
        if nums[i] == val:
            i += 1
        else:
            nums[front_ind] = nums[i]
            front_ind += 1
            i += 1
            k += 1
    return k


print(removeElement(None, [0,1,2,2,3,0,4,2], 2))