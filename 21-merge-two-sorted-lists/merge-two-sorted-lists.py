# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=dummy=ListNode()
        while list1 and list2:
            val1=list1.val
            val2=list2.val
            if val1>=val2:
                curr.next=ListNode(val2)
                list2=list2.next
                curr=curr.next
            else:
                curr.next=ListNode(val1)
                list1=list1.next
                curr=curr.next
        if list1 and not list2:
            curr.next=list1
        
        if list2 and not list1:
            curr.next=list2
        
        return dummy.next