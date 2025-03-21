def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return []

    def backtrack(cur, left, right):
        if left == right == n:
            results.append(cur)
            return

        if left < n:
            new_str = cur + "("
            backtrack(new_str, left + 1, right)
        if left > right:
            new_str = cur + ")"
            backtrack(new_str, left, right + 1)

    results = []
    cur = ""
    backtrack(cur, 0, 0)
    return results
