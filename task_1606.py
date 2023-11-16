from heapq import heappop, heappush

from sortedcontainers import SortedList


def busiestServers1(self, k, arrival, load):
    work_time = [0 for i in range(k)]
    arrive = [0 for i in range(k)]
    count = [0 for i in range(k)]
    job = 0
    for arrive_time, cost in zip(arrival, load):
        target = job % k
        # NO JOB
        if work_time[target] == 0:
            work_time[target] = cost
            arrive[target] = arrive_time
            count[target] += 1
        else:
            # FINISH
            if arrive_time >= arrive[target] + work_time[target]:
                work_time[target] = cost
                arrive[target] = arrive_time
                count[target] += 1
            # NOT FINISH
            else:
                search = target + 1
                if search == k:
                    search = 0
                while search != target:
                    if work_time[search] == 0:
                        work_time[search] = cost
                        arrive[search] = arrive_time
                        count[search] += 1
                        break
                    else:
                        # FINISH
                        if arrive_time >= arrive[search] + work_time[search]:
                            work_time[search] = cost
                            arrive[search] = arrive_time
                            count[search] += 1
                            break
                        else:
                            search += 1
                            if search == k:
                                search = 0
        job += 1
    max_work = max(count)
    return [i for i, req in enumerate(count) if req == max_work]


def busiestServers2(self, k, arrival, load):
    available = SortedList(range(k))
    busy = []
    requests = [0] * k
    for i, (start, t) in enumerate(zip(arrival, load)):
        while busy and busy[0][0] <= start:
            available.add(busy[0][1])
            heappop(busy)
        if len(available) == 0:
            continue
        j = available.bisect_left(i % k)
        if j == len(available):
            j = 0
        id = available[j]
        requests[id] += 1
        heappush(busy, (start + t, id))
        available.remove(id)
    maxRequest = max(requests)
    return [i for i, req in enumerate(requests) if req == maxRequest]


def busiestServers3(self, k, arrival, load):
    free = SortedList(range(k))
    work = []
    count = [0 for i in range(k)]
    job = -1
    for arrive, cost in zip(arrival, load):
        job += 1
        while work and work[0][0] <= arrive:
            free.add(work[0][1])
            heappop(work)
        if len(free) == 0:
            continue
        index = free.bisect_left(job % k)
        if index == len(free):
            index = 0
        index = free[index]
        count[index] += 1
        heappush(work, (arrive + cost, index))
        free.remove(index)

    max_work = max(count)
    return [i for i, req in enumerate(count) if req == max_work]


print(busiestServers3(None, 3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2]))