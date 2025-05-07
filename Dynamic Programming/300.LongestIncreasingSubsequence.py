def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i - 1):
            if nums[i] > nums[j]:
                # 对于每个i来说，他的dp最大值其实就是他之前每一位能凑出来的longest subsequence。
                # 对于之前每一位来说，他可以选这一位或者不选
                dp[j] = max(dp[j - 1] + 1, dp[i])

    return dp[-1]
