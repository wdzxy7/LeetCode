def findMedianSortedArrays(self, nums1, nums2):
    nums1 += nums2
    nums1.sort()
    l = len(nums1)
    if l % 2 == 0:
        return (nums1[l // 2 - 1] + nums1[l // 2]) / 2
    else:
        return nums1[l // 2]
print(findMedianSortedArrays(None, [1,2], [3,4]))