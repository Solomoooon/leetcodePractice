def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total / 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, nums - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
