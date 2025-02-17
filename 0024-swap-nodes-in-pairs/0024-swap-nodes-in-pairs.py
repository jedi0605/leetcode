# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumn = ListNode(0,head)
        pre, curr = dumn,head

        while curr and curr.next:
            # save ptr
            nextPair = curr.next.next
            sec = curr.next
            # reverse
            curr.next = nextPair
            sec.next = curr
            pre.next = sec
            # move
            pre = curr
            curr = nextPair
        return dumn.next            