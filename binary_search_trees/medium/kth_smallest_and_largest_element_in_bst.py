import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray



# Kth Smallest and Largest element in BST

class Solution:

    def inorderTraversal(self, root, inorder):
        if root:
            self.inorderTraversal(root.left, inorder)
            inorder.append(root.data)
            self.inorderTraversal(root.right, inorder)

    # Time Complexity: O(n) | Space Complexity: O(n)
    def kLargesSmall(self, root, k):
        inorder = []
        self.inorderTraversal(root, inorder)
        kth_smallest = inorder[k-1]
        kth_largest = inorder[len(inorder)-k]
        return [kth_smallest, kth_largest]




if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root =  [3,1,4,None,2]
    k = 1

    root = buildTreeFromArray(root)
    print(sol.kLargesSmall(root, k))


    # Test 2
    root = [5, 3, 6, 2, None, None, None, 1]
    k = 3

    root = buildTreeFromArray(root)
    print(sol.kLargesSmall(root, k))
