from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    i, j = 0, 0
    mergedArr = []
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and j < len(nums2) and nums1[i] <= nums2[j]:
            mergedArr.append(nums1[i])
            i += 1
        elif j < len(nums2):
            mergedArr.append(nums2[j])
            j += 1
        elif i < len(nums1):
            mergedArr.append(nums1[i])
            i += 1
    print(mergedArr)
    if len(mergedArr) % 2 == 0:
        return (mergedArr[len(mergedArr) // 2] + mergedArr[len(mergedArr) // 2 - 1]) / 2
    else:
        return mergedArr[len(mergedArr) // 2]


print(findMedianSortedArrays([1, 3], [2]))
