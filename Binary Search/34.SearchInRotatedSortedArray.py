from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    def binarySearch(left, right, target, lower):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # 找到一个match
                if lower:
                    # 这个表示是在找low bound
                    if mid == 0 or nums[mid - 1] != target:
                        # 如果mid是第一个，或者左边的不等于target
                        return mid
                    else:
                        right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        # # 如果mid是最后一个，或者右边的不等于target
                        return mid
                    else:
                        left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    lower = binarySearch(left, right, target, True)
    higher = binarySearch(left, right, target, False)
    return (lower, higher)


nums = [1]
target = 1
print(searchRange(nums, target))
