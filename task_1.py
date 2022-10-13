def twoSum(self, nums, target):
    num_dict = {}
    for i in range(len(nums)):
        try:
            num_dict[nums[i]].append(i)
            num_dict[nums[i]][0] = 2
        except:
            num_dict[nums[i]] = [1, i]
    for i in num_dict.keys():
        try:
            next_num = target - i
            ind = num_dict[next_num]
            if ind == num_dict[i] and num_dict[i][0] == 1:
                continue
            elif ind == num_dict[i] and num_dict[i][0] == 2:
                return num_dict[i][1], num_dict[i][2]
            return num_dict[i][1], ind[1]
        except:
            pass
    return None, None


a, b = twoSum(None, [3,2,4], 6)
print(a, b)