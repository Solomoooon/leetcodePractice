# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        dummy = ListNode()
        ans = dummy

        while node1 or node2:
            cur = ListNode(
                min(node1.val if node1 else math.inf, node2.val if node2 else math.inf)
            )
            if node1 and (not node2 or node1.val < node2.val):
                node1 = node1.next
            else:
                node2 = node2.next
            ans.next = cur
            ans = ans.next

        return dummy.next
