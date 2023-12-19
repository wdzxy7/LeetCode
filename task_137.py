def singleNumber(self, nums):
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums) - 1, 3):
        if nums[i] != nums[i + 1] or nums[i + 1] != nums[i + 2]:
            return nums[i] ^ nums[i + 1] ^ nums[i + 2]
    return nums[-1]

print(singleNumber(None, [30000,500,100,30000,100,30000,100]))