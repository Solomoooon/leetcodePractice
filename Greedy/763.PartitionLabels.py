def partitionLabels(self, s: str) -> List[int]:
    lastOccurence = {}
    for i, char in enumerate(s):
        lastOccurence[char] = i

    # 遍历记录每个字母最后出现的位置

    partition_end = 0
    partition_start = 0
    answer = []
    for i, char in enumerate(s):
        partition_end = max(partition_end, lastOccurence[char])
        # 不断更新partition的位置
        # 注意如果当前走过的路程里partition_end一直在变大，那么i == partition_end的条件不会被满足直到真的走到了这个字母最后出现位置

        if i == partition_end:
            # 说明前面的部分可以被partition了
            answer.append(i - partition_start + 1)
            # answer存每个partition的长度
            partition_start = partition_end + 1
            # partition_start记录从上一次partition到当前的距离

    return answer
