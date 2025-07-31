def canJump(self, nums: List[int]) -> int:
    n = len(nums)
    cur_far = 0

    for i in range(n):
        if i > cur_far:
            # cur_far根本到不了当前位置
            return False

        cur_far = max(cur_far, i + nums[i])
        # cur_far表示能到达的最远位置

        if cur_far >= n - 1:
            # 说明已经至少能到结尾的位置了
            return True
