def search(self, nums, target):
    if target in nums:
        return True
    else:
        return False

print(search(None, [2,5,6,0,0,1,2], 3))