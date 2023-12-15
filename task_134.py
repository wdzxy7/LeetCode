def canCompleteCircuit(self, gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start = 0
    res = 0
    for i in range(len(gas)):
        res += (gas[i] - cost[i])
        if res < 0:
            res = 0
            start = i + 1
    return start

print(canCompleteCircuit(None, [1,2,3,4,5], [3,4,5,1,2]))