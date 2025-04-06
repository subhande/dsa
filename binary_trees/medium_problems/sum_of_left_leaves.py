# Sum Of left leaves

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeavesHelper(self, node, left_child):
        if node and node.left is None and node.right is None:
            return node.val if left_child is True else 0
        if node is None:
            return 0
        return self.sumOfLeftLeavesHelper(node.left, True) + self.sumOfLeftLeavesHelper(node.right, False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.sumOfLeftLeavesHelper(root, left_child=False)
