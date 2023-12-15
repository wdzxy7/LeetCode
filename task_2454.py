import heapq
from heapq import heappop, heappush


def secondGreaterElement(self, nums):
    if len(nums) < 3:
        return [-1] * len(nums)
    search_stack = []
    res = [-1, -1]
    search_stack.append(nums[-1])
    search_stack.append(nums[-2])
    stack_max = []
    heapq.heappush(stack_max, nums[-1])
    heapq.heappush(stack_max, nums[-2])
    for i in range(len(nums) - 3, -1, -1):
        t_stack = []
        count = 0
        if nums[i] >= stack_max[0]:
            res.insert(0, -1)
            if not search_stack[-1] == search_stack[-2] and nums[i] == search_stack[-1]:
                pass
            else:
                search_stack.append(nums[i])
            heapq.heappop(stack_max)
            heapq.heappush(stack_max, nums[i])
            continue
        while search_stack:
            t = search_stack.pop()
            if t > nums[i]:
                count += 1
            t_stack.append(t)
            if count == 2:
                res.insert(0, t)
                break
        if count != 2:
            res.insert(0, -1)
        while t_stack:
            search_stack.append(t_stack.pop())
        if search_stack[-1] == search_stack[-2] and nums[i] == search_stack[-1]:
            pass
        else:
            search_stack.append(nums[i])
    return res

def secondGreaterElement2(self, nums):
    res = [-1] * len(nums)
    stack = []
    q = []

    for i in range(len(nums)):
        while len(q) and q[0][0] < nums[i]:
            res[q[0][1]] = nums[i]
            heappop(q)
        while len(stack) and nums[stack[-1]] < nums[i]:
            heappush(q, (nums[stack[-1]], stack[-1]))
            stack.pop()
        stack.append(i)

    return res



print(secondGreaterElement2(None, [2,4,0,9,6]))
