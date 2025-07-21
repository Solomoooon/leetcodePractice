def orangesRotting(self, grid: List[List[int]]) -> int:
    def bfs(grid, row, col, ini):
        if (
            row < 0
            or col < 0
            or row > len(grid)
            or col > len(grid[0])
            or grid[row][col] == "0"
            or grid[row][col] == "1"
            and ini == True
        ):
            return 0
        if grid[row][col] == 1:
            grid[row][col] = 2

            s1 = 1 + bfs(grid, row + 1, col, False)
            s2 = 1 + bfs(grid, row - 1, col, False)
            s3 = 1 + bfs(grid, row, col + 1, False)
            s4 = 1 + bfs(grid, row, col - 1, False)

        return min(s1, min(s2, min(s3, s4)))

    found = False
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            temp = bfs(grid, i, j, True)
            count += temp

    if count == 0 or any(
        grid[row][col] == 1 for row in range(len(grid)) for col in range(len(grid[0]))
    ):
        return -1

    else:
        return count


def orangesRotting(self, grid: List[List[int]]) -> int:
    max_time = 0
    row = len(grid)
    col = len(grid[0])
    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        i, j, time = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                queue.append((ni, nj, time + 1))
                max_time = max(max_time, time + 1)
                grid[ni][nj] = 2

    for r in grid:
        if 1 in r:
            return -1
    return max_time
