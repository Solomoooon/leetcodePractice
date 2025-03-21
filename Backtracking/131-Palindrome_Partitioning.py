def partition(self, s: str) -> List[List[str]]:
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
        # if s == reverse(s)

    def dfs(s, path, result):
        if len(s) == 0:
            result.append(path)
            return

        for i in range(1, len(s) + 1):
            if isPalindrome(s[:i]):
                dfs(s[i:], path + [s[:i]], result)

    result = []
    dfs(s, [], result)
    return result
