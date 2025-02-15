import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


#TODO: Implement more optimal solution


# Insert a given node in BST

class Solution:
    # Time Complexity: O(h) | Space Complexity: O(h)
    def insertIntoBSTRecrsive(self, root, val):
        # Add a new node with the given value to the BST
        if not root:
            return TreeNode(val)
        # Check if the value is less than the root node's value
        if val < root.data:
            root.left = self.insertIntoBSTRecrsive(root.left, val)
        # Check if the value is greater than the root node's value
        else:
            root.right = self.insertIntoBSTRecrsive(root.right, val)
        return root
    # Time Complexity: O(h) | Space Complexity: O(1)
    def insertIntoBSTIterative(self, root, val):
        if not root:
            return TreeNode(val)
        current = root
        while True:
            # Traverse the BST to find the correct position to insert the new node
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
        return root



if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root = [4, 2, 7, 1, 3]
    val = 5
    root = buildTreeFromArray(root)
    print(sol.insertIntoBSTRecrsive(root, val))
    print(sol.insertIntoBSTIterative(root, val))

    # Test 2
    root =  [40, 20, 60, 10, 30, 50, 70]
    val = 25
    root = buildTreeFromArray(root)
    print(sol.insertIntoBSTRecrsive(root, val))
    print(sol.insertIntoBSTIterative(root, val))
