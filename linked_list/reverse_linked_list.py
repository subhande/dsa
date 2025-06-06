# Reverse Linked List
# Prev -> Curr -> Next Pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next # 3
            curr.next = prev # 1 -> None
            prev = curr # 1
            curr = next_temp # 3
            # 1 <- 2 -> 3
        return prev
