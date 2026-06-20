from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        prev, curr = None, l1

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            # curr.next, prev, curr  = prev, curr, curr.next

        l1 = prev

        prev, curr = None, l2

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            # curr.next, prev, curr  = prev, curr, curr.next

        l2 = prev

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

        prev, curr = None, dummyHead.next

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = None
        while head:
            # Keep the next node
            temp = head.next
            # Reverse the link
            head.next = prev
            # Update the previous node and the current node.
            prev = head
            head = temp
        return prev

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        total_sum = 0
        carry = 0
        ans = ListNode()
        while r1 or r2:
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next

            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans
