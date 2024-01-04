def findDuplicate(self, nums):
    fast = nums[nums[0]]
    slow = nums[0]
    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
    slow = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
    return fast

print(findDuplicate(None, [1,3,4,2,2]))