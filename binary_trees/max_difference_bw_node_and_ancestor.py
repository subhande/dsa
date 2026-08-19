# Max Difference B/W Node and Ancestor


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        self.maxDiff = 0

        def maxAncestorDiffHelper(node: TreeNode | None) -> tuple:
            if node is None:
                return float("inf"), float("-inf")
            if node.left is None and node.right is None:
                return node.val, node.val

            leftMinValue, leftMaxValue = maxAncestorDiffHelper(node.left)
            rightMinValue, rightMaxValue = maxAncestorDiffHelper(node.right)

            leftDiff = (
                max(abs(node.val - leftMaxValue), abs(node.val - leftMinValue))
                if leftMinValue != float("inf")
                else 0
            )
            rightDiff = (
                max(abs(node.val - rightMaxValue), abs(node.val - rightMinValue))
                if rightMinValue != float("inf")
                else 0
            )

            self.maxDiff = max(self.maxDiff, max(leftDiff, rightDiff))

            return min(node.val, min(leftMinValue, rightMinValue)), max(
                node.val, max(leftMaxValue, rightMaxValue)
            )

        maxAncestorDiffHelper(root)
        return self.maxDiff


class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(
                self.result, abs(cur_max - node.val), abs(cur_min - node.val)
            )
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result


class Solution3:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)
