# Validate Binary Search Tree


class Solution:
    def isValidBSTHelper(
        self, node: TreeNode | None, minValue: float | int, maxValue: float | int
    ) -> bool:
        if node is None:
            return True
        valid = True
        if node.val <= minValue or node.val >= maxValue:
            valid = False
        if node.left and node.left.val >= node.val:
            valid = False
        if node.right and node.right.val <= node.val:
            valid = False

        isLeftSubTreeValidBST = self.isValidBSTHelper(node.left, minValue, node.val)

        isRightSubTreeValidBST = self.isValidBSTHelper(node.right, node.val, maxValue)

        return valid and isLeftSubTreeValidBST and isRightSubTreeValidBST

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)

        return validate(root)
