def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if len(text1) == 0 or len(text2) == 0:
        return 0
    memo = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    memo[0][0] = 1 if text1[0] == text2[0] else 0
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text2))):
            if text1[row] == text2[col]:
                memo[row][col] = memo[row + 1][col + 1]
                # 这道题解题思路是反过来的，从两个string结尾开始。
                # 如果两个str当前一位相等，那么就等于他们右下方的memo[row + 1][col + 1] +1
            else:
                memo[row][col] = max(memo[row + 1][col], memo[row][col + 1])
                # 如果不相等，那就取右侧和下方的最大值

    return memo[0][0]
