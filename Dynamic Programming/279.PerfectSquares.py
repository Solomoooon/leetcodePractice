def numSquares(self, n: int) -> int:
    square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
    # 解题思路是如果当前算的是n的结果，那就先把n以下的所有perfect square都算出来。
    # 然后从1一直到n-1，看看那个需要的perfect square个数最少
    dp = [float("inf")] * (n + 1)
    # float的数字最大值，一共n+1个
    dp[0] = 0
    for i in range(1, n + 1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)
            # 用dp的方式, dp[i]等于自己或者减当前perfect square后（这算一个perfect square所以+1）后再需要的步骤

    return dp[-1]
