# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode()
        dummy.next=head
        slow=head
        fast=head.next

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        end=slow.next
        slow.next=None

        prev=None
        slow.next=None
        while end:
            tmp = end.next
            end.next = prev
            prev = end
            end = tmp

        first, end = head, prev
        while end:
            tmp1, tmp2 = first.next, end.next
            first.next = end
            end.next = tmp1
            first, end = tmp1, tmp2


    