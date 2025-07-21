def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(grid, row, col):
        if (
            row < 0
            or col < 0
            or row > len(grid)
            or col > len(grid[0])
            or grid[row][col] != "1"
        ):
            return

        grid[row][col] = "0"
        # 当前位置遍历过改成0，防止重复dfs

        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row, col - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                # 这道题的核心就是每一个island一定是单拎出来一块的陆地，所以需要几次dfs完成整个图就有几个island
                count += 1
    return count
