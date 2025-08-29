# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode()
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        for i in range(len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next

        return ans.next
