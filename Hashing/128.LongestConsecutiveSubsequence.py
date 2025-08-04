def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    # 把所有数字存到一个set里，这样访问时间为O(1)
    answer = 0
    for num in num_set:
        if num - 1 not in num_set:
            # 如果比他小一个的数不在set里，说明这个是一个consecutive subsequence的开始
            length = 1
            cur = num + 1
            while cur in num_set:
                # 只要比他大一个的一直在set里，继续增加consecutive subsequence的长度
                length += 1
                cur += 1

            answer = max(answer, length)

    return answer
