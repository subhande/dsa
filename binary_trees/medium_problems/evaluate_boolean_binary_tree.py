# Evaluate Boolean Binary Tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        leftSubTreeValue = rightSubTreeValue = None
        if root.left is None and root.right is None:
            return root.val == 1
        if root.left is not None:
            leftSubTreeValue = self.evaluateTree(root.left)
        if root.left is not None:
            rightSubTreeValue = self.evaluateTree(root.right)
        return leftSubTreeValue or rightSubTreeValue if root.val == 2 else leftSubTreeValue and rightSubTreeValue
