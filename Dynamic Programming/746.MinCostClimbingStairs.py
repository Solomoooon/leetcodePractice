def minCostClimbingStairs(self, cost: List[int]) -> int:
    if len(cost) == 1:
        return cost[0]
    n = len(cost)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
