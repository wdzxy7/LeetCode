def maxProduct(self, nums):
    max_arr = [0 for i in range(len(nums))]
    max_arr[0] = nums[0]
    min_arr = max_arr.copy()
    for i in range(1, len(nums)):
        max_arr[i] = max(max_arr[i - 1] * nums[i], min_arr[i - 1] * nums[i], nums[i])
        min_arr[i] = min(max_arr[i - 1] * nums[i], min_arr[i - 1] * nums[i], nums[i])
    return max(max_arr)


print(maxProduct(None, [-2,3,0,5,6,7,0,-3,5,-7,-4]))