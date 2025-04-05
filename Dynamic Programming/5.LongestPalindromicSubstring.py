def longestPalindrome(self, s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    # 用一个2D array表示这个string
    ans = [0, 0]

    for i in range(n):
        dp[i][i] = True
        # 每个长度为1的string都是palindrome

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = [i, i + 1]
            # 如果跟一个字符串跟他相邻的相同，那么这是一个长度为2的palindrome

    for diff in range(2, n):
        # 第一层循环的是每个字符串首尾的距离，最小为2，最大为n-1
        for i in range(n - diff):
            # 第二层循环的就是首位的位置，最小为0，最大为n-diff-1
            j = i + diff
            # 那么相对应的尾部的位置就是i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                # 这里的if有两个条件因为新添加的首尾要相等，同时之前的部分本身也必须是palindrome
                dp[i][j] = True
                ans = [i, j]
    i, j = ans
    return s[i : j + 1]
