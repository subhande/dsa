import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


# Search in BST
class Solution:
    def searchBST(self, root, val):
        while root:
            if root.data == val:
                return root
            elif val < root.data:
                root = root.left
            else:
                root = root.right
        return None


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root = [4, 2, 7, 1, 3]
    val = 2
    root = buildTreeFromArray(root)
    print(sol.searchBST(root, val))


    # Test 2
    root = [4, 2, 7, 1, 3]
    val = 5
    root = buildTreeFromArray(root)
    print(sol.searchBST(root, val))
