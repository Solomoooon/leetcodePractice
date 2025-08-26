# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    ans = cur = ListNode()
    for l in lists:
        while l:
            heapq.heappush(heap, l.val)
            l = l.next
            # 用heap把所有node的值存进去

    while heap:
        heap_node = ListNode(heapq.heappop(heap))
        # 每一次heap pop一个最小值，把它创建成一个新的node不断放进cur所在的链表里
        cur.next = heap_node
        cur = cur.next
        # 通过cur = cur.next不断加入新的ordered nodes
    return ans.next


# 因为cur遍历的链表的首位有效字母是ans.next
