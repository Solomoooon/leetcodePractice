def jump(self, nums: List[int]) -> int:
    answer = 0
    n = len(nums)
    cur_far, cur_end = 0, 0
    # cur_far表示当前当前这一步能达到的最远距离
    # cur_end表示当前这一跳的边界
    for i in range(n - 1):
        cur_far = max(cur_far, i + nums[i])

        if i == cur_end:
            # 这个表示如果当前这一跳已经当边界了，就需要跳一次了
            cur_end = cur_far
            answer += 1

    return answer
