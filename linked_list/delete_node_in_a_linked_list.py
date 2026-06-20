# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach 1:
# Time Complexity: O(n) | Space Complexity: O(1)


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prevNode = None
        while node.next:
            node.val = node.next.val
            prevNode = node
            node = node.next

        if prevNode:
            prevNode.next = None


# Approach 2:
# Time Complexity: O(1) | Space Complexity: O(1)
class Solution2:
    def deleteNode(self, node):
        # Overwrite data of next node on current node.
        node.val = node.next.val
        # Make current node point to next of next node.
        node.next = node.next.next
