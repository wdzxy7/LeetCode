def removeDuplicates(self, nums):
    write = 1
    count = 1
    pre = nums[0]
    for i in range(1, len(nums)):
        if count == 2:
            if nums[i] == pre:
                continue
            else:
                count = 1
                nums[write] = nums[i]
                write += 1
        elif nums[i] == pre:
            nums[write] = nums[i]
            count += 1
            write += 1
        else:
            nums[write] = nums[i]
            count = 1
            write += 1
        pre = nums[i]
    return write



print(removeDuplicates(None, [1,1,1,2,2,3]))