# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_p, slow_p = head.next, head
        while fast_p and slow_p:
            if fast_p == slow_p:
                return True
            slow_p = slow_p.next
            if fast_p.next != None:
                fast_p = fast_p.next.next
            else:
                break

        return False
