import sys


def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max(curr * max_so_far, curr * min_so_far))
        # temp_max有三种情况：1.curr就是最大的；2.之前的max_so_far和curr都是正的或者都是负数；3.curr和min_so_far一正一负构成新的可能的最大乘积
        min_so_far = min(curr, min(curr * min_so_far, curr * max_so_far))
        # min_so_far与上面同理

        max_so_far = temp_max
        result = max(max_so_far, result)

    return result
