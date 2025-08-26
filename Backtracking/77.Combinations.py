def combine(self, n: int, k: int) -> List[List[int]]:

    results = []

    def backtrack(start, cur):
        if len(cur) == k:
            results.append(list(cur))
            return

        for i in range(start, n + 1):
            if i not in cur:
                cur.append(i)
                backtrack(i, cur)
                cur.pop()

    backtrack(1, [])
    return results
