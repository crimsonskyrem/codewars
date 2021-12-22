def findMedianSortedArrays(nums1, nums2):
    tmp = []
    total = len(nums1) + len(nums2)
    median = total // 2 + 1
    for _ in range(median):
        if nums1 and nums2 and nums1[0] < nums2[0]:
            tmp.append(nums1.pop(0))
        elif nums1 and not nums2:
            tmp.append(nums1.pop(0))
        else:
            tmp.append(nums2.pop(0))
    if total % 2:
        return tmp[-1]
    else:
        return (tmp[-1] + tmp[-2]) / 2

print(findMedianSortedArrays([1,3],[3,4]))