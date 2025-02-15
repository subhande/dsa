
import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


# Check if a tree is a BST or not

class Solution:
    def isBSTUtil(self, root, min, max):
        if root is None:
            return True

        if root.data <= min or root.data >= max:
            return False

        return self.isBSTUtil(root.left, min, root.data) and self.isBSTUtil(root.right, root.data, max)

    def isBST(self, root):
        return self.isBSTUtil(root, float("-inf"), float("inf"))



if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root = [2, 1, 3]
    root = buildTreeFromArray(root)
    print(sol.isBST(root)) # True

    # Test 2
    root = [5, 1, 4, None, None, 3, 6]
    root = buildTreeFromArray(root)
    print(sol.isBST(root)) # False
