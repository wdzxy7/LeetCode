import heapq


def furthestBuilding(self, heights, bricks, ladders):
    n = len(heights)
    queue = []
    sums = 0
    for i in range(1, n):
        val = heights[i] - heights[i - 1]
        if val > 0:
            heapq.heappush(queue, val)
        if len(queue) > ladders:
            sums += heapq.heappop(queue)
        if sums > bricks:
            return i - 1
    return n - 1


print(furthestBuilding(None, [1,5,1,2,3,4,10000], 4, 1))