
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy  # Pointer to build the merged list
        heap = []

        # Step 1: Insert the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # (value, index, node)

        # Step 2: Process the heap
        while heap:
            val, i, node = heapq.heappop(heap)  # Get the smallest node
            curr.next = node  # Append it to the result list
            curr = curr.next  # Move the pointer

            if node.next:  # If there are more nodes, push the next one into the heap
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next  # Return the merged list

