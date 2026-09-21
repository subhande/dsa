# In order successor in BST II
#
#
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# Time Complexity: O(h) | Space Complexity: O(1)
# Two cases:
# 1. If the node has a right child, then the successor is the leftmost node in the right subtree. -> GO DOWN
# 2. If the node does not have a right child, then the successor is one of its ancestors. We need to traverse up the tree until we find
# a node that is the left child of its parent. The parent of that node will be the successor. -> GO UP


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Optional[Node]":

        successor = None
        # Go down the tree to find the successor. Leftmost node in the right subtree
        if node.right is not None:
            successor = node.right
            while successor.left is not None:
                successor = successor.left

        else:
            # Go up the tree to find the successor. The first ancestor that is a left child of its parent
            while node.parent and node == node.parent.right:
                node = node.parent
            successor = node.parent

        return successor
