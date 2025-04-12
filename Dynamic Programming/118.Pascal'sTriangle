def generate(self, numRows: int) -> List[List[int]]:
    ans = []
    for i in range(numRows):
        level = []
        for j in range(i + 1):
            if j == 0 or j == i:
                level.append(1)
            else:
                level.append(ans[i - 1][j - 1] + ans[i - 1][j])

        ans.append(level)
    return ans
