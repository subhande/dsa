from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        node = head

        size = 0
        while node:
            node = node.next
            size += 1
        if size == 1:
            return None

        node = head
        # Remove head
        if size - n == 0:
            return head.next
        for i in range(size - n - 1):
            node = node.next

        # Remove middle or tail
        node.next = node.next.next
        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummay = ListNode(0)
        dummay.next = head
        head = dummay

        node = head

        size = 0
        while node:
            node = node.next
            size += 1

        node = head

        for i in range(size - n - 1):
            node = node.next

        # Remove middle or tail or head
        node.next = node.next.next
        return head.next
