from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddList = ListNode(0)
        evenList = ListNode(0)
        oddCurrNode = oddList
        evenCurrNode = evenList

        count = 0
        while head:
            if count % 2 == 1:
                oddCurrNode.next = head
                oddCurrNode = oddCurrNode.next
            else:
                evenCurrNode.next = head
                evenCurrNode = evenCurrNode.next

            head = head.next
            count += 1

        evenCurrNode.next = None
        oddCurrNode.next = None
        evenCurrNode.next = oddList.next

        return evenList.next


class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:  # even and odd
            # 1. Link the current odd node to the next odd node (which is the node after the current even node).
            # 2. Move the odd pointer to the next odd node.
            # 3. Link the current even node to the next even node (which is the node after the new odd node).
            # 4. Move the even pointer to the next even node.
            # Diagram:
            # Before iteration:
            # odd -> odd.next (even) -> even.next (next odd) -> even.next.next (next even) -> even.next.next.next (next odd) ...
            # After iteration:
            # curr odd -> next odd (even.next)
            # curr even -> next even (odd.next or even.next.next)
            odd.next = even.next
            odd = odd.next
            even.next = odd.next  # even.next.next
            even = even.next

        odd.next = evenHead

        return head
