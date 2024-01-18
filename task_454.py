def fourSumCount(self, nums1, nums2, nums3, nums4):
    sum_dict = {}
    for i in nums1:
        for j in nums2:
            s = i + j
            try:
                sum_dict[s] += 1
            except:
                sum_dict[s] = 1
    count = 0
    for i in nums3:
        for j in nums4:
            s = i + j
            if -s in sum_dict:
                count += sum_dict[-s]
    return count

print(fourSumCount(None, [-1,-1], [-1, 1], [-1, 1], [1,-1]))