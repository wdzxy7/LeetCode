def canJump(self, nums):
    l = len(nums)
    if l == 1:
        return True
    far = [0 for i in range(l)]
    for i in range(len(nums) - 1):
        now_index = i
        change_index = []
        far_index = far[now_index]
        while now_index < l:
            if nums[now_index] == 0:
                change_index.append(now_index)
                break
            elif far[now_index] == 0 or far[now_index] < nums[now_index] + now_index:
                change_index.append(now_index)
                next_index = now_index + nums[now_index]
                now_index = next_index
                far_index = next_index
            else:
                far_index = far[now_index]
                break
        if len(change_index) != 0:
            for index in range(change_index[0], change_index[-1] + 1):
                far[index] = far_index
        if far_index >= l - 1:
            return True
        if far[i] < i + 1:
            return False
    return False

print(canJump(None, [3,0,0,0]))