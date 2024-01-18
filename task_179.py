import functools


def largestNumber(self, nums):
    nums = [str(i) for i in nums]
    nums.sort(reverse=True)
    if nums[0] == '0':
        return '0'
    def cmp(a, b):
        if a + b == b + a:
            return 0
        elif a + b > b + a:
            return 1
        else:
            return -1
    nums.sort(key=functools.cmp_to_key(cmp), reverse=True)
    return ''.join(nums)

print(largestNumber(None, [0, 0, 1, 30, 30, 3]))