# Maximum path sum


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSumHelper(self, root, sums):
        if root is None:
            return 0
        leftSubTreeSum = max(0, self.maxPathSumHelper(root.left, sums))
        rightSubTreeSum = max(0, self.maxPathSumHelper(root.right, sums))
        sums[0] = max(sums[0], leftSubTreeSum + rightSubTreeSum + root.val)
        return max(leftSubTreeSum, rightSubTreeSum) + root.val
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def maxPathSum(self, root):
        sums = [float("-inf")]
        self.maxPathSumHelper(root, sums)
        return sums[0]
