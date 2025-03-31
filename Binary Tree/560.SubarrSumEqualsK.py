def subarraySum(self, nums: List[int], k: int) -> int:
    curr_sum = 0
    count = 0
    h = defaultdict(int)
    for i in range(0, len(nums)):
        curr_sum += nums[i]
        if curr_sum == k:
            count += 1
        count += h[curr_sum - k]
        h[curr_sum] += 1

    return count
