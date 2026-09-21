# Trim a Binary Search Tree

# Example 1: low = 6 | high = 8
#               8
#             /   \
#            3     9
#           / \
#          1   5
#           \ / \
#           2 4  6
#                 \
#                  7

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Recursive approach to trim a binary search tree
# Time Complexity: O(n) | Space Complexity: O(h)
class Solution:

    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        if not root:
            return None

        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        elif root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        return root
         

