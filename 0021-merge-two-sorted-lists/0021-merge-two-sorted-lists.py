# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        dummy = head
        while list1!=None and list2!=None:
            cur1 = list1
            cur2 = list2
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next                
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1!=None:
            head.next = list1
        if list2!=None:
            head.next = list2
        return dummy.next