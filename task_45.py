def jump(self, nums):
    front = 0
    end = nums[0]
    jump_count = 0
    while front < len(nums) - 1:
        max_dis = 0
        for i in range(front + 1, end + 1):
            if i >= len(nums):
                break
            max_dis = max(max_dis, i + nums[i])
        front = end
        end = max_dis
        jump_count += 1
    return jump_count

print(jump(None, [1, 2, 3]))