# Reversed Linked List II
# Prev -> Curr -> Next Pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev = None
        curr = head

        leftStarted = False
        rightReached = False

        leftNode = None
        rightNode = None

        leftPrevNode = None

        while curr:

            if leftStarted is False and rightReached is False:
                if curr.val == left:
                    leftStarted = True
                    leftNode = curr
                    leftPrevNode = prev
                prev = curr
                curr = curr.next
            elif leftStarted and rightReached is False:
                if curr.val == right:
                    rightReached = True
                    rightNode = curr
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            else:
                leftPrevNode.next = prev
                leftNode.next = curr
                break
        return head
