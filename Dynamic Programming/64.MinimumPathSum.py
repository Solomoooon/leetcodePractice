def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    d = [[0] * n for _ in range(m)]
    d[0][0] = grid[0][0]
    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row][col] + min(grid[row - 1][col], grid[row][col])
    return grid[m - 1][n - 1]


def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    d = [[0] * n for _ in range(m)]
    # 这道题用的是逆向推理法，题目问的是从左上到右下，我们推理是反过来。
    # 所以一个格子的dp推理的值可能是源自他的右边，下边，或者右边以及下边的最小值
    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if row == m - 1 and col != n - 1:
                # 这个格是最右边的，所以他的dp值只能来自下边的格
                d[row][col] = grid[row][col] + d[row][col + 1]
            elif col == n - 1 and row != m - 1:
                # 这个格是最下边的，所以他的dp值只能来自右边的格
                d[row][col] = grid[row][col] + d[row + 1][col]
            elif row != m - 1 and col != n - 1:
                # 这个格在中间的位置，所以他的dp推理值取决于右边和下边那个推理值更小
                d[row][col] = grid[row][col] + min(d[row + 1][col], d[row][col + 1])
            else:
                d[row][col] = grid[row][col]
    return d[0][0]
