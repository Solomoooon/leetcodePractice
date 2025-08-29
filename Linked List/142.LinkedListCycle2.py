# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeDict = set()
        cur = head
        count = 0
        while cur:
            if cur in nodeDict:
                return cur

            nodeDict.add(cur)
            count += 1
            cur = cur.next

        return
