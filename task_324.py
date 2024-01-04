def wiggleSort(self, nums):
    nums.sort()
    sert = 1
    while sert < len(nums):
        nums.insert(sert, nums[-1])
        del nums[-1]
        sert += 2
    return nums

print(wiggleSort(None, [1,5,1,1,6,4]))