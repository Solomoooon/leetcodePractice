def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    ans = 0
    index = 0
    maxDiagnoal = 0
    for i in range(len(dimensions)):
        diagonal = math.sqrt(dimensions[i][0] ** 2 + dimensions[i][1] ** 2)
        if diagonal > maxDiagnoal:
            index = i
            maxDiagnoal = diagonal
            ans = dimensions[index][0] * dimensions[index][1]
        elif diagonal == maxDiagnoal:
            ans = max(ans, dimensions[i][0] * dimensions[i][1])

    return ans
