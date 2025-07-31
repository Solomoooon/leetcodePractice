def maxProfit(self, prices: List[int]) -> int:
    minPrice = prices[0]
    answer = 0

    for i in range(1, len(prices)):
        minPrice = min(minPrice, prices[i])
        # minPrice是遍历到目前为止最小的价格
        answer = max(answer, prices[i] - minPrice)
        # 如果此时价格差最大，更新answer的值

    return answer
