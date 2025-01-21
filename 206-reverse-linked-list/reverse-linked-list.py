class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev,cur=None,head
        # while cur:
        #     nex=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nex
        # return prev
        if not head:
            return None

        newHead=head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead