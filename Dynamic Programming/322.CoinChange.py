from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        # 这里注意！很重要的一点！coin这层for必须要写在外面,因为反过来的话可能导致dp[i]过早更新
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp)
    return dp[amount] if dp[amount] != float("inf") else -1


coins = [474, 83, 404, 3]
amount = 264

print(coinChange(coins, amount))
