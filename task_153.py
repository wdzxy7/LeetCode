from typing import List


def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    if l == r:
        return nums[0]
    t_min = float('inf')
    while l < r:
        mid = (l + r) // 2
        t_min = min(t_min, nums[l], nums[r])
        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            break
        if nums[mid] > nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return min(t_min, nums[mid])


print(findMin(None, [4,5,6,7,0,1,2]))