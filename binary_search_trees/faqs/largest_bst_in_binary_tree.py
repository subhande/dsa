import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


# Largest BST in Binary Tree

class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:
    def largestBSTHelper(self, root):
        if not root:
            return NodeValue(float("inf"), float("-inf"), 0)

        left = self.largestBSTHelper(root.left)
        right = self.largestBSTHelper(root.right)

        if left.maxNode < root.data < right.minNode:
            return NodeValue(min(left.minNode, root.data), max(right.maxNode, root.data), left.maxSize + right.maxSize + 1)
        else:
            return NodeValue(float("-inf"), float("inf"), max(left.maxSize, right.maxSize))
    # Time complexity: O(n) | Space complexity: O(n) + O(h) for additional info and recursive call stack
    def largestBST(self, root):
        return self.largestBSTHelper(root).maxSize


if __name__ == "__main__":
    # Example 1:
    # Input: [10, 5, 15, 1, 8, None, 7]
    # Output: 3
    # Explanation: The largest BST is the subtree [5, 1, 8].
    root = buildTreeFromArray([10, 5, 15, 1, 8, None, 7])
    print(Solution().largestBST(root))  # Output: 3

    # Example 2:
    # Input: [10, 5, 15, 1, 8, 7, 17]
    # Output: 7
    # Explanation: The whole tree is a BST.
    root = buildTreeFromArray([10, 5, 15, 1, 8, 7, 17])
    print(Solution().largestBST(root))  # Output: 7
