def permute(self, nums: List[int]) -> List[List[int]]:

    def backtrack(cur):
        if len(cur) == len(nums):
            results.append(cur[:])
            return
        for num in nums:
            if num not in cur:
                cur.append(num)
                backtrack(cur)
                cur.pop()

    results = []
    backtrack([])
    return results
