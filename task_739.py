import heapq
from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0 for i in range(len(temperatures))]
    temp_list = []
    heapq.heappush(temp_list, (temperatures[0], 0))
    for i in range(1, len(temperatures)):
        while True:
            if len(temp_list) != 0:
                top = heapq.heappop(temp_list)
                if top[0] < temperatures[i]:
                    res[top[1]] = i - top[1]
                else:
                    heapq.heappush(temp_list, top)
                    heapq.heappush(temp_list, (temperatures[i], i))
                    break
            else:
                heapq.heappush(temp_list, (temperatures[i], i))
                break
    return res

print(dailyTemperatures(None, [73,74,75,71,69,72,76,73]))