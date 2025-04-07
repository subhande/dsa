# Swap Nodes In Pairs
# Prev -> Curr -> Next Pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        curr = head.next
        prev_prev = None
        count = 0
        while curr:

            temp_next = curr.next # 3 # None
            curr.next = prev # 2 -> 1 # 4 -> 3
            prev.next = temp_next # None
            if prev_prev:
                prev_prev.next = curr
            prev_prev = prev


            prev = temp_next
            if count == 0:
                head = curr

            curr = temp_next.next if temp_next else None
            count += 1
            print([prev], [curr])
        return head

        return
