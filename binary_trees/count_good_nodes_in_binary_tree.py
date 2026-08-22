from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# Count Good Nodes in Binary Tree
class Solution:
    def __init__(self) -> None:
        self.numOfgoodNodes: int = 0

    def goodNodesHelper(self, node: TreeNode | None, maxTillNow: float) -> None:
        if node is None:
            return
        if node.val >= maxTillNow:
            self.numOfgoodNodes += 1
        maxTillNow = max(maxTillNow, node.val)
        self.goodNodesHelper(node.left, maxTillNow)
        self.goodNodesHelper(node.right, maxTillNow)

    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodesHelper(root, float("-inf"))
        return self.numOfgoodNodes
