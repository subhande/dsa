

# Construct a BT from Postorder and Inorder
#
from utils import buildTreeFromArray, TreeNode

from collections import deque

class Solution:
    def buildTree(self, postorder, inorder):
        if len(inorder) != len(postorder):
            return None

        inorderMap = {val: idx for idx, val in enumerate(inorder) }

        def helper(postStart, postEnd, inStart, inEnd):
            # Base case
            if postStart > postEnd or inStart > inEnd:
                return None

            # The last element in the postorder traversal is the root
            root = TreeNode(postorder[postEnd])

            # Find the index of the root in the inorder traversal
            rootIdx = inorderMap[postorder[postEnd]]

            leftSubtreeSize = rootIdx - inStart

            root.left = helper(postStart, postStart + leftSubtreeSize - 1, inStart, rootIdx - 1)
            root.right = helper(postStart + leftSubtreeSize, postEnd - 1, rootIdx + 1, inEnd)

            return root

        return helper(0, len(postorder) - 1, 0, len(inorder) - 1)




if __name__ == "__main__":
    sol = Solution()

    # Test 1
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    expectedOutput = buildTreeFromArray([3, 9, 20, None, None, 15, 7])
    result = sol.buildTree(postorder, inorder)
    print(result)
    assert result == expectedOutput, f"Test 1 failed: expected {expectedOutput}, but got {result}"

    # Test 2
    postorder = [5, 6, 4, 9, 2, 3]
    inorder = [5, 4, 6, 3, 2, 9]
    expectedOutput = buildTreeFromArray([3, 4, 2, 5, 6, None, 9])
    result = sol.buildTree(postorder, inorder)
    assert result == expectedOutput, f"Test 2 failed: expected {expectedOutput}, but got {result}"
    print(result)
