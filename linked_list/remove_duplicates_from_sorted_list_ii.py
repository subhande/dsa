from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n) | Space Complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        uniqueList = ListNode(1000)

        uniqueListCurrNode = uniqueList

        node = head

        prevNode = None
        prevNodeCount = 0
        currentNodeCount = 0

        while node is not None:
            if prevNode and prevNode.val != node.val:
                if prevNodeCount == 1:
                    uniqueListCurrNode.next = prevNode
                    uniqueListCurrNode = uniqueListCurrNode.next
                    # 1. Ensure the next pointer of the last unique node is set to None to avoid linking to duplicates
                    # uniqueListCurrNode.next = None
                currentNodeCount = 0

            currentNodeCount += 1
            prevNode = node
            prevNodeCount = currentNodeCount
            node = node.next
        if prevNodeCount == 1:
            uniqueListCurrNode.next = prevNode
            uniqueListCurrNode = uniqueListCurrNode.next
        # 2. Ensure the next pointer of the last unique node is set to None to avoid linking to duplicates
        uniqueListCurrNode.next = None

        # Make sure either 1 or 2 is done to avoid linking to duplicates. Either one of them is enough.
        return uniqueList.next


class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node
        # before the sublist of duplicates
        pred = sentinel

        while head:
            # If it's the beginning of a duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next

                # Skip all duplicates
                pred.next = head.next

            # Otherwise, move predecessor
            else:
                pred = pred.next

            # move forward
            head = head.next

        return sentinel.next
