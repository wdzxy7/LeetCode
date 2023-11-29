def trap(self, height):
    l = len(height)
    high = [0 for i in range(l)]
    low = [0 for i in range(l)]
    high[0] = height[0]
    for i in range(1, l):
        high[i] = max(high[i - 1], height[i])
    low[-1] = height[-1]
    for i in range(l - 2, -1, -1):
        low[i] = max(height[i], low[i + 1])
    water = 0
    for i in range(l):
        water += min(high[i], low[i]) - height[i]
    return water

print(trap(None, [0,1,0,2,1,0,1,3,2,1,2,1]))