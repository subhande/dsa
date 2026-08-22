# Sum root to leaf numbers


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.allPathSum = 0

    def sumNumbersHelpers(self, node: Optional[TreeNode], currPathSum: int) -> int:
        if node is None:
            return

        currPathSum += str(node.val)

        if node.left is None and node.right is None:
            self.allPathSum += int(currPathSum)

        if node.left:
            self.sumNumbersHelpers(node.left, currPathSum)

        if node.right:
            self.sumNumbersHelpers(node.right, currPathSum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumNumbersHelpers(root, "")
        return self.allPathSum
