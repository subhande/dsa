# Linked List Cycle

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next.next if head.next else None
        slow = head.next

        while fast and slow:
            if fast == slow:
                return True
            fast = fast.next.next if fast.next else None
            slow = slow.next
        return False
