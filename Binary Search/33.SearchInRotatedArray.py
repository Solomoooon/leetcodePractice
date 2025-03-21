def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
            # 说明从0到left-1是一个ordered array，然后之后是另一个rotated sorted array
        else:
            right = mid - 1
    print("mid = ", mid)

    def binarySearch(left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
            return binarySearch(left, right, target)
        else:
            left = mid + 1
            return binarySearch(left, right, target)

    ans1 = binarySearch(0, left - 1, target)
    if ans1 != -1:
        return ans1
    else:
        return binarySearch(left, len(nums) - 1, target)
