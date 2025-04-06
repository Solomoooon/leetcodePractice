def longestValidParentheses(self, s: str) -> int:
    dp = [0] * len(s)
    ans = 0

    for i in range(1, len(s)):
        if s[i] == ")":
            # 如果当前位置是)的话，我们可以检查之前的位置了
            if s[i - 1] == "(":
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # 如果上一位是(的话，那么有两种情况。
                # 如果i是第二位之前，dp[i] = 2；否则dp[i] = dp[i-2] + 2，因为dp[i-2]可能也是一个valid substr，那么把当前这个也加上
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                # 如果把当前位置往dp[i-1]去推的话，推完之后的再上一位是(的话
                dp[i] = (
                    dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                )
                # 这个时候有两种情况。第一种是i往前推dp[i-1]后还大于2，
                # 那么因为s[i]已经跟s[i - dp[i - 1] - 1] == "("连接上了（这个时候无论如何要+2），我们看s[i - dp[i - 1] - 2]是否也是valid string，如果是的话就可以拼起来
            ans = max(ans, dp[i])
    return ans
