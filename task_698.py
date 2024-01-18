def canPartitionKSubsets(self, nums, k):
    if sum(nums) % k:
        return False
    d = sum(nums) // k
    nums.sort(reverse=True)
    edge = [0 for i in range(k)]
    def search(index):
        nonlocal edge
        if index == len(nums):
            return True
        for i in range(k):
            if i and edge[i] == edge[i - 1]:
                continue
            edge[i] += nums[index]
            if edge[i] <= d and search(index + 1):
                return True
            edge[i] -= nums[index]
        return False
    return search(0)

print(canPartitionKSubsets(None, [3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2], 10))