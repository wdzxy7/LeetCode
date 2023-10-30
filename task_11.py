def maxArea(height):
    length = len(height)
    front = 0
    back = length - 1
    max_water = 0
    while front < back:
        h = min(height[front], height[back])
        water = h * (length - 1)
        if water > max_water:
            max_water = water
        if height[front] < height[back]:
            front += 1
            length -= 1
        else:
            back -= 1
            length -= 1
    return max_water


print(maxArea([1,1]))