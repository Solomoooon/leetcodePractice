from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left
    # left的值符合所有情况：target在nums里，不在nums里（比所有数都小，比所有数都大，在两个数之间）


nums = [1, 3]
target = 0
print(searchInsert(nums, target))
