def subsets(self, nums: List[int]) -> List[List[int]]:
    results = []

    def backtrack(start, comb):
        results.append(list(comb))
        # 第一种情况是只包含到start目前为止的一个subset

        for i in range(start, len(nums)):
            comb.append(nums[i])
            # 第二种是包含nums[i]的情况
            backtrack(i + 1, comb)
            comb.pop()
            # 第三种是不包含nums[i]的情况，随着i不断更新start的值，添加各种不包含nums[i]的情况

    backtrack(0, [])
    return results
