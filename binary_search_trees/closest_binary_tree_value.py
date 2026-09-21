
# Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closestValue = float("inf")
        delta = float("inf")

        node = root

        while node:
            newDelta = abs(node.val - target)
            if newDelta < delta:
                closestValue = node.val
                delta = newDelta
            elif newDelta == delta:
                closestValue = min(node.val, closestValue)
                delta = newDelta
            if target < node.val:
                node = node.left
            else:
                node = node.right

        return closestValue
