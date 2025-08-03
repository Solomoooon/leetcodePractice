def twoSum(self, nums: List[int], target: int) -> List[int]:
    Seen = {}
    for i, num in enumerate(target):
        if target - num in Seen:
            return [Seen[target - num], i]

        Seen[num] = i
