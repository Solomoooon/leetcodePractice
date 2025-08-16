def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequency = Counter(nums)
    # python内置的Counter可以记录nums里每个数字出现的频率

    n = len(nums)
    bucket = [[] for _ in range(n + 1)]
    for num, count in frequency.items():
        # for x, y in frequency.items()也是一样的，x表示数字本身，y表示出现的频率
        bucket[count].append(num)
        # 用bucket把出现频率一样的数字存起来

    ans = []
    for i in range(n, 0, -1):
        # 从频率最多的往后数（频率最多为n次）
        for num in bucket[i]:
            ans.append(num)
            # 先放一个进去，因为ans的初始长度为1
            if len(ans) == k:
                # 如果已经装够里top k个数字，return ans
                return ans
