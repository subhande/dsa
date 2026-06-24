# Reversed Linked List II
# Prev -> Curr -> Next Pointers

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def reverseBetween(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            # If con is None, then we are changing the first node (head) of the LinkedList
            head = prev
        tail.next = cur
        return head


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        prev = None
        curr = head

        leftStarted = False
        rightReached = False

        leftNode = None
        rightNode = None

        leftPrevNode = None

        count = 1

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
