import heapq


def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = []
    # python的heap是默认找最小值
    for i in range(len(nums)):
        heapq.heappush(heap, -nums[i])
        #

    for j in range(k):
        if j == k - 1:
            return -1 * heappop(heap)
        else:
            heappop(heap)
