# Sum Of left leaves


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeavesHelper(
        self, node: TreeNode | None, leftChild: bool = False
    ) -> int:

        if node and node.left is None and node.right is None:
            return node.val if leftChild is True else 0
        if node is None:
            return 0
        return self.sumOfLeftLeavesHelper(node.left, True) + self.sumOfLeftLeavesHelper(
            node.right, False
        )

    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return self.sumOfLeftLeavesHelper(root, leftChild=False)
