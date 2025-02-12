# Check for balanced binary tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isBalancedHelper(self, root):
        if root is None:
            return 0, True
        leftSubTreeHeight, leftSubTreeBalanced = self.isBalancedHelper(root.left)
        rightSubTreeHeight, rightSubTreeBalanced = self.isBalancedHelper(root.right)
        height = 1 + max(leftSubTreeHeight, rightSubTreeHeight)
        diff = abs(leftSubTreeHeight - rightSubTreeHeight)
        balanced = diff <= 1 and leftSubTreeBalanced and rightSubTreeBalanced
        return height, balanced
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def isBalanced(self, root):
        _, balanced = self.isBalancedHelper(root)
        return balanced


class Solution2:
    def dfsHeight(self, root):
        if root is None:
            return 0
        leftSubTreeHeight = self.dfsHeight(root.left)
        if leftSubTreeHeight == -1:
            return -1
        rightSubTreeHeight = self.dfsHeight(root.right)
        if rightSubTreeHeight == -1:
            return -1
        if abs(leftSubTreeHeight - rightSubTreeHeight) > 1:
            return -1
        return 1 + max(leftSubTreeHeight, rightSubTreeHeight)
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def isBalanced(self, root):
        height = self.dfsHeight(root)
        return height != -1


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(15)
    root.right.right.right = TreeNode(7)
    # root.right.right.right.right = TreeNode(7)

    s = Solution1()

    print(s.isBalanced(root))

    s = Solution2()

    print(s.isBalanced(root))
