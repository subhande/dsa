# Min Distance Between BST Nodes
# Minimum Absolute Difference in BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:

        inorder = []
        stack = []

        node = root

        while True:

            if node is not None:
                stack.append(node)
                node = node.left
            elif len(stack) > 0:
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
            else:
                break
        minDiff = float("inf")

        for idx in range(1, len(inorder)):
            minDiff = min(minDiff, inorder[idx] - inorder[idx-1])
    
        return minDiff

        