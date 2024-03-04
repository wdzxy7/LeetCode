def circularArrayLoop(self, nums):
    for i in range(len(nums)):
        visit = [False] * len(nums)
        j = i
        move = nums[i]
        start = i
        move_count = 0
        while True:
            if visit[j]:
                if start == j:
                    if move_count > 1:
                        return True
                    else:
                        break
                else:
                    break
            visit[j] = True
            j = j + nums[j]
            if j >= len(nums):
                j = j % len(nums)
            elif j < 0:
                j = j % len(nums)
            # diff
            if nums[j] < 0 < move or move < 0 < nums[j]:
                break
            move_count += 1
    return False
print(circularArrayLoop(None,[-1,-2,-3,-4,-5,6]))