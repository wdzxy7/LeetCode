def minCostClimbingStairs(self, cost):
    if len(cost) == 2:
        return min(cost[0], cost[1])
    step_cost = [cost[0], cost[1]]
    all_cost = 0
    cost[0] = 0
    cost[1] = 0
    for i in range(2, len(cost) + 1):
        all_cost = min(step_cost[0] + cost[i - 2], step_cost[1] + cost[i - 1])
        step_cost[0] = step_cost[1]
        step_cost[1] = all_cost
    return all_cost


print(minCostClimbingStairs(None, [10,15,20]))