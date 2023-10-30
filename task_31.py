def nextPermutation(self, nums) -> None:
    l = len(nums)
    for i in range(l - 1, -1, -1):
        if nums[i - 1] >= nums[i]:
            continue
        elif i == 0:
            nums = sorted(nums)
        else:
            change_ind = i - 1
            change_num = min(nums[i:])
            min_ind = nums[i:].index(change_num) + l - i + 1
            nums[min_ind] = nums[change_ind]
            nums[change_ind] = change_num
            nums[i:] = sorted(nums[i:])
            break
    return nums


print(nextPermutation(None, [3,2,1]))