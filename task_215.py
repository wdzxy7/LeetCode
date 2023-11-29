import heapq


def findKthLargest(self, nums, k):
    arr = []
    for num in nums:
        heapq.heappush(arr, num)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


print(findKthLargest(None, [3,2,3,1,2,4,5,5,6], 4))