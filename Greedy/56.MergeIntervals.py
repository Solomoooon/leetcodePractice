def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    answer = []
    partition_start = 0
    partition_end = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] > intervals[i - 1][1]:
            answer.append(answer[partition_start][0], answer[i][1])
            partition_start = i + 1

    if len(answer) != 0:
        return answer
    return intervals
