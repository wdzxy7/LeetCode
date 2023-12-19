def rotate(self, nums, k):
    if k > len(nums):
        k = k % len(nums)
    sub_arr = nums[:k]
    write = k - 1
    for i in range(len(nums) - 1, k - 1, -1):
        nums[write] = nums[i]
        write -= 1
        if write == -1:
            write = len(nums) - 1
    sub_i = k - 1
    for i in range(k):
        nums[write] = sub_arr[sub_i]
        write -= 1
        if write == -1:
            write = len(nums) - 1
        sub_i -= 1
    return nums

print(rotate(None, [1, 2], 5))