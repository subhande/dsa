from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0 or head is None:
            return head
        headNode = None
        tailNode = None
        lastNode = None

        n = 0
        node = head
        while node:
            lastNode = node
            node = node.next
            n += 1

        k = k % n if k > n else k

        if n == 1 or n == k or k == 0:
            return head

        node = head
        for _ in range(n - k - 1):
            node = node.next
        headNode = node.next
        tailNode = node
        lastNode.next = head
        tailNode.next = None

        return headNode


class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head
