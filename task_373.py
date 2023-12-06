import heapq


def kSmallestPairs(self, nums1, nums2, k):
    nums1 = [i for i in range(1, 10001)]
    nums2 = [i for i in range(1, 10001)]
    arr = []
    count = 0
    t_max = -1
    for i in nums1:
        for j in nums2:
            s = i + j
            if count >= k:
                if s > -arr[0][0]:
                    break
                else:
                    heapq.heappop(arr)
                    heapq.heappush(arr, [-s, i, j])
            else:
                heapq.heappush(arr, [-s, i, j])
            if s > t_max:
                t_max = s
            count += 1
    res = []
    for i in range(min(k, len(arr))):
        res.append(heapq.heappop(arr)[1:])
    return res

print(kSmallestPairs(None, [1,7,11], [2,4,6], 3))