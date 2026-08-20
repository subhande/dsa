# Count Good Nodes in Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodesHelper(self, node: TreeNode | None, maxTillNow: float | int) -> None:
        if node is None:
            return
        if node.val >= maxTillNow:
            self.numOfgoodNodes += 1
        maxTillNow = max(maxTillNow, node.val)
        self.goodNodesHelper(node.left, maxTillNow)
        self.goodNodesHelper(node.right, maxTillNow)

    def goodNodes(self, root: TreeNode) -> int:
        self.numOfgoodNodes = 0
        self.goodNodesHelper(root, float("-inf"))
        return self.numOfgoodNodes
