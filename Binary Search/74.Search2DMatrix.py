def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    # number of rows
    if m == 0:
        return False
    n = len(matrix[0])
    # number of columns
    left = 0
    right = m * n - 1
    size = m * n

    while left <= right:
        mid = (left + right) // 2
        cur = matrix[mid // n][mid % n]
        # row是mid整除n，column是mid除以n的余数（行内偏移了几位）
        if cur == target:
            return True
        elif cur > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
