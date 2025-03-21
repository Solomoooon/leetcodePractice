def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    results = []

    def backtrack(remain, comb, start):
        if remain == 0:
            # 满足条件存在results里
            results.append(list(comb))
            return
        elif remain < 0:
            # 不满足条件
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()

    backtrack(target, [], 0)

    return results
