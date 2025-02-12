# Diameter of Binary Tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution1:
    def diameterOfBinaryTreeHelper(self, root, maxPathlength):
        if root is None:
            return 0, max(0, maxPathlength)

        leftSubTreeHeight, leftSubTreeMaxPathLength = self.diameterOfBinaryTreeHelper(root.left, maxPathlength)
        rightSubTreeHeight, rightSubTreeMaxPathLength = self.diameterOfBinaryTreeHelper(root.right, maxPathlength)

        currentTreePathLength = leftSubTreeHeight + rightSubTreeHeight
        currentSubTreeHeight = 1 + max(leftSubTreeHeight, rightSubTreeHeight)
        maxPathlength = max(currentTreePathLength, leftSubTreeMaxPathLength, rightSubTreeMaxPathLength, maxPathlength)
        return currentSubTreeHeight, maxPathlength

    def diameterOfBinaryTree(self, root):
        _, maxPathlength = self.diameterOfBinaryTreeHelper(root, float("-inf"))
        return maxPathlength




class Solution2:
    def diameterOfBinaryTreeHelper(self, root, diameter):
        if root is None:
            return 0
        leftSubTreeHeight = self.diameterOfBinaryTreeHelper(root.left, diameter)
        rightSubTreeHeight = self.diameterOfBinaryTreeHelper(root.right, diameter)
        diameter[0] = max(diameter[0], leftSubTreeHeight + rightSubTreeHeight)
        return 1 + max(leftSubTreeHeight, rightSubTreeHeight)

    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.diameterOfBinaryTreeHelper(root, diameter)
        return diameter[0]



if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(15)
    # root.right.right.right = TreeNode(7)
    # root.right.right.right.right = TreeNode(7)

    s = Solution1()

    print(s.diameterOfBinaryTree(root))

    s = Solution2()

    print(s.diameterOfBinaryTree(root))
