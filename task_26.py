def removeDuplicates(self, nums):
    k = 1
    i = 1
    front = nums[0]
    front_ind = 0
    while i < len(nums):
        if nums[i] == front:
            i += 1
        else:
            nums[front_ind + 1] = nums[i]
            front = nums[i]
            i += 1
            front_ind += 1
            k += 1
    return k, nums[0:k]


print(removeDuplicates(None, [-1, -1, 0, 0]))