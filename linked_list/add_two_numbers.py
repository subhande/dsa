from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode(val=0, next=None)
        curr_l3 = l3

        while l1 or l2:
            new_val = curr_l3.val
            if l1:
                new_val += l1.val
                l1 = l1.next
            if l2:
                new_val += l2.val
                l2 = l2.next
            digit = new_val % 10
            curr_l3.val = digit
            new_node = ListNode(val=new_val // 10, next=None)
            if new_node.val != 0 or l1 is not None or l2 is not None:
                curr_l3.next = new_node
                curr_l3 = new_node
        return l3


class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        carry = 0

        dummyHead = ListNode(0)

        currNode = dummyHead

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            colSum = l1_val + l2_val + carry
            carry = 1 if colSum >= 10 else 0
            colSum = colSum - 10 if colSum >= 10 else colSum

            currNode.next = ListNode(colSum)
            currNode = currNode.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            currNode.next = ListNode(1)
            currNode = currNode.next

        return dummyHead.next
