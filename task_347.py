import collections
import heapq


def topKFrequent(self, nums, k):
    count = collections.Counter(nums)
    heap = [(val, key) for key, val in count.items()]
    return [item[1] for item in heapq.nlargest(k, heap)]


print(topKFrequent(None, [1,1,1,2,2,3], 2))