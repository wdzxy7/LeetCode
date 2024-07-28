def maxMoves(self, grid):
    res = [[float('-inf') for i in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(grid)):
        res[i][0] = 0
    for row in range(len(grid[0])): # 右
        for col in range(len(grid)): # 上下
            node = grid[col][row]
            pre_step = res[col][row]
            if col - 1 >= 0 and row + 1 < len(grid[0]):
                if grid[col - 1][row + 1] > node:
                    res[col - 1][row + 1] = max(res[col - 1][row + 1], pre_step + 1)
            if row + 1 < len(grid[0]):
                if grid[col][row + 1] > node:
                    res[col][row + 1] = max(res[col][row + 1], pre_step + 1)
            if col + 1 < len(grid) and row + 1 < len(grid[0]):
                if grid[col + 1][row + 1] > node:
                    res[col + 1][row + 1] = max(res[col + 1][row + 1], pre_step + 1)
    max_value = 0
    for i in res:
        max_value = max(max_value, max(i))
    return max_value

print(maxMoves(None, [[65,200,263,220,91,183,2,187,175,61,225,120,39],[111,242,294,31,241,90,145,25,262,214,145,71,294],[152,25,240,69,279,238,222,9,137,277,8,143,143],[189,31,86,250,20,63,188,209,75,22,127,272,110],[122,94,298,25,90,169,68,3,208,274,202,135,275],[205,20,171,90,70,272,280,138,142,151,80,122,130],[284,272,271,269,265,134,185,243,247,50,283,20,232],[266,236,265,234,249,62,98,130,122,226,285,168,204],[231,24,256,101,142,28,268,82,111,63,115,13,144],[277,277,31,144,49,132,28,138,133,29,286,45,93],[163,96,25,9,3,159,148,59,25,81,233,127,12],[127,38,31,209,300,256,15,43,74,64,73,141,200]]))