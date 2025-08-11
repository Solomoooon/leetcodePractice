def subarraySum(self, nums: List[int], k: int) -> int:
    answer = 0
    curr_sum = 0
    prefix_sum = defaultdict(int)
    # 用dictionary的hashing获取速度是O(1)。整个算法的复杂度是O(n)

    for i in range(len(nums)):
        curr_sum += nums[i]
        # 到当前位置i的和
        if curr_sum == k:
            answer += 1
        # 如果从头到i这一位置正好等于k，那么answer + 1

        answer += prefix_sum[curr_sum - k]
        # 这个是核心，表示的是之前遍历过的部分里有几个位置j是之后的部分能加k得到当前curr_sum。
        # 因为是subarray所以过去的部分里哪个数想选都可以
        prefix_sum[curr_sum] += 1
        # curr_sum的出现次数加一
    return answer
