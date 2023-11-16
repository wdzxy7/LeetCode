def countMaxOrSubsets(self, nums):
    max_or, count = 0, 0
    def search(t_or, num_list):
        nonlocal max_or, count
        if t_or > max_or:
            max_or = t_or
            count = 1
        elif t_or == max_or:
            count += 1
        for i in range(len(num_list)):
            temp = t_or | num_list[i]
            search(temp, num_list[i + 1:])
    search(0, nums)
    return count

print(countMaxOrSubsets(None, [2,2,2]))