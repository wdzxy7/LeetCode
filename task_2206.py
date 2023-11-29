def divideArray(self, nums):
    num_dict = {}
    for i in nums:
        try:
            num_dict[i] += 1
        except:
            num_dict[i] = 1
    for key in num_dict.keys():
        if num_dict[key] % 2 == 1:
            return False
    return True

print(divideArray(None, [3,2,3,2,2,2]))