from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            # Move slow pointer by 1 and fast pointer by 2
            slow = slow.next
            fast = fast.next.next
        return slow
