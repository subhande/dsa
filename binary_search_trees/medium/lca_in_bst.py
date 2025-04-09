import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray

# LCA in BST

class Solution:
    # Time Complexity: O(h) | Space Complexity: O(1)
    def lca(self, root, p, q):
        # Initialize the current pointer to start at the root of the BST.
        current = root

        # Iterate down the tree until we find the lowest common ancestor.
        while current:
            # If current node's data matches either p or q,
            # then it must be the LCA (because one node is an ancestor of itself).
            if current.data == p or current.data == q:
                return current

            # If one key is on the left subtree and the other is on the right subtree,
            # then the current node is the LCA.
            elif (p < current.data and q > current.data) or (p > current.data and q < current.data):
                return current

            # If both keys are less than current.data,
            # move to the left subtree because both nodes lie there.
            elif p < current.data and q < current.data:
                current = current.left

            # If both keys are greater than current.data,
            # move to the right subtree because both nodes lie there.
            elif p > current.data and q > current.data:
                current = current.right

        # If the while loop finishes without returning,
        # it indicates that the BST did not contain either p or q fully,
        # and None (or current which is now None) is returned.
        return current





if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root =  buildTreeFromArray([5, 3, 6, 2, 4, None, 7])
    p = 2
    q = 4
    print(sol.lca(root, p, q)) # 2

    # Test 2
    root = buildTreeFromArray([5, 3, 6, 2, 4, None, 7])
    p = 3
    q = 7
    print(sol.lca(root, p, q)) # 5
