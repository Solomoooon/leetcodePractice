# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = []
        count = 0
        ans = cur = ListNode()
        while head:
            if count < k:
                temp.append(head.val)
                head = head.next
                count += 1
            else:
                count = 0
                temp = []

        reversed_arr = [row[::-1] for row in arr]

        for i in range(len(reversed_arr)):
            for num in reversed_arr:
                cur.next = ListNode(num)
                cur = cur.next

        return ans.next


def reverse(head, k):
    new_head, ptr = None, head
    ptr.next = new_head
    new_head = ptr

    ptr
