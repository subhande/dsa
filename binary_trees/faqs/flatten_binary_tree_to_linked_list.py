
# Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node
        leftTail = self.preorder(node.left)
        rightTail = self.preorder(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        return rightTail if rightTail else leftTail





    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.preorder(root)
