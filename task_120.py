def minimumTotal(self, triangle):
    pre = [0]
    length = 1
    for line in triangle:
        for i in range(length):
            if i == 0:
                line[i] = line[i] + pre[0]
            elif i == length - 1:
                line[i] = line[i] + pre[-1]
            else:
                line[i] = min(line[i] + pre[i], line[i] + pre[i - 1])
        pre = line
        length += 1
    return min(pre)

print(minimumTotal(None, [[2],[3,4],[6,5,7],[4,1,8,3]]))