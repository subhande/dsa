# Range Sum Of BST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
# Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
# Wrost case h = n for skewed tree or chain tree, best case h = log(n) for balanced tree
class Solution:
    def __init__(self):
        self.result = 0

    def helper(self, node: Optional[TreeNode], low: int, high: int):

        if not node:
            return

        ele = node.val

        if low <= ele <= high:
            self.result += ele

        if low < ele < high:
            self.helper(node.left, low, high)
            self.helper(node.right, low, high)
        elif ele <= low:
            self.helper(node.right, low, high)
        elif ele >= high:
            self.helper(node.left, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.helper(root, low, high)

        return self.result


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        ans = 0
        dfs(root)
        return ans
