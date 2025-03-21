def subsets(self, nums: List[int]) -> List[List[int]]:
    results = []

    def backtrack(start, comb):
        results.append(comb[:])

        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(i + 1, comb)
            comb.pop()

    comb = []
    backtrack(0, comb)
    return results
