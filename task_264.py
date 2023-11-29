import heapq


def nthUglyNumber(self, n):
    arr = [1,2,3,4,5]
    if n <= 5:
        return arr[n - 1]
    else:
        arr.clear()
        heapq.heappush(arr, 1)
        heapq.heappush(arr, 2)
        heapq.heappush(arr, 3)
        heapq.heappush(arr, 4)
        heapq.heappush(arr, 5)
    pre = 0
    while n > 1:
        t = heapq.heappop(arr)
        if t == pre:
            continue
        else:
            pre = t
            heapq.heappush(arr, t * 2)
            heapq.heappush(arr, t * 3)
            heapq.heappush(arr, t * 5)
            n -= 1
    while True:
        t = heapq.heappop(arr)
        if t == pre:
            continue
        else:
            break
    return t


print(nthUglyNumber(None, 10))