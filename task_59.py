def generateMatrix(self, n):
    array = [[-1 for i in range(n)] for i in range(n)]
    head_l = 0
    head_r = n - 1
    down_l = 0
    down_r = n - 1
    num = 1
    while head_l < head_r:
        for i in range(head_l, head_r):
            array[head_l][i] = num
            num += 1
        for i in range(head_l, down_r + 1):
            array[i][down_r] = num
            num += 1
        for i in range(down_r - 1, down_l, -1):
            array[down_r][i] = num
            num += 1
        for i in range(head_r, head_l, -1):
            array[i][head_l] = num
            num += 1
        head_l += 1
        head_r -= 1
        down_l += 1
        down_r -= 1
    if array[head_l][head_r] == -1:
        array[head_l][head_r] = num
    return array

print(generateMatrix(None, 2))