def uniquePaths(self, m: int, n: int) -> int:
    d = [[1] * n for _ in range(m)]
    # 初始是每个格都为1

    for row in range(1, m):
        # 我们是从d[0][0]开始，到这里以及d[0][1]和d[1][0]每个有且只有一种可能性。
        for col in range(1, n):
            d[row][col] = d[row - 1][col] + d[row][col - 1]
            # 到每一个格的可能性次数等于到他上边和左边两个格可能性次数的和

    return d[m - 1][n - 1]
