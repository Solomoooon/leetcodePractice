# 超时办法
# def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#     def solve(pos):
#         if pos == len(s):
#             return True
#         for i in range(pos + 1, len(s) + 1):
#             if s[pos:i] in wordDict:
#                 solve(i)
#                 if solve(i):
#                     return True
#         return False

#     return solve(0)


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * len(s)
    for i in range(len(s)):
        for word in wordDict:
            if i < len(word) - 1:
                # 这个是防止string s已经快到头了，word比remaining string长。后面比较会出错
                continue

            if i == len(word) - 1 or dp[i - len(word)]:
                # 第一种情况适用于第一个发现的word match，第二种适用于这个词从往前推的话，上一个dp位置也可行
                if s[i - len(word) + 1 : i + 1] == word:
                    # 记住！string切片 s[起始位置：终点位置（不包含），step size]
                    # 如果从上一个位置开始到当前位置的substring等于word的话，dp[i] = True
                    dp[i] = True
                    break
    return dp[-1]
