

# Construct a BT from Preorder and Inorder
#
from utils import buildTreeFromArray, TreeNode

from collections import deque

# Construct a BT from Preorder and Inorder

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def buildTree(self, preorder, inorder):
        # Create a map to store indices
        # of elements in the inorder traversal
        inorderMap = {val: idx for idx, val in enumerate(inorder) }

        # Recursive helper function to build the tree
        def helper(preStart, preEnd, inStart, inEnd):
            # Base case
            if preStart > preEnd or inStart > inEnd:
                return None

            # The first element in the preorder traversal is the root
            root = TreeNode(preorder[preStart])

            # Find the index of the root in the inorder traversal
            rootIdx = inorderMap[root.data]

            # Calculate the number of elements in the left subtree
            leftSubtreeSize = rootIdx - inStart

            # Recursively build the left and right subtrees
            root.left = helper(preStart + 1, preStart + leftSubtreeSize, inStart, rootIdx - 1)
            root.right = helper(preStart + leftSubtreeSize + 1, preEnd, rootIdx + 1, inEnd)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    expectedOutput = buildTreeFromArray([3, 9, 20, None, None, 15, 7])
    result = sol.buildTree(preorder, inorder)
    assert result == expectedOutput, f"Test 1 failed: expected {expectedOutput}, but got {result}"
    # print(result)

    # Test 2
    preorder = [3, 4, 5, 6, 2, 9]
    inorder = [5, 4, 6, 3, 2, 9]
    expectedOutput = buildTreeFromArray([3, 4, 2, 5, 6, None, 9])
    result = sol.buildTree(preorder, inorder)
    assert result == expectedOutput, f"Test 2 failed: expected {expectedOutput}, but got {result}"
    # print(result)
