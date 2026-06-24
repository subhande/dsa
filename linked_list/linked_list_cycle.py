# Linked List Cycle

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Best Solution: Using Floyd's Cycle Detection Algorithm
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


# Alternative Solution: Takes more iterations to find the cycle
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            # Move slow pointer by 1 and fast pointer by 2
            slow = slow.next
            fast = fast.next.next
        return False
