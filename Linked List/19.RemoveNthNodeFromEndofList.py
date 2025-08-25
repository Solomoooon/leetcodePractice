# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        arr = []
        count = 0
        while node:
            arr.append(node)
            count += 1
            last = node
            node = node.next

        if n == len(arr):
            print(1)
            return head.next
        if n == 1:
            arr[len(arr) - 2].next = None
            return head
        arr[len(arr) - n - 1].next = arr[len(arr) - n + 1]
        return head
