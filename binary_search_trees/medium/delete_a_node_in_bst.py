import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray



# Delete a node in BST

class Solution:
    def findSuccessor(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Time Complexity: O(h) | Space Complexity: O(h)
    def deleteNode(self, root, key):
        if not root:
            return None

        # Traverse the tree to locate the node to delete.
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with the key is found.
            # Case 1: Node with only one child or no child.
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: Node with two children.
            # Find the inorder successor (smallest in the right subtree).
            successor = self.findSuccessor(root.right)

            # Replace root's value with successor's value.
            root.data = successor.data
            # Delete the inorder successor.
            root.right = self.deleteNode(root.right, successor.data)
        return root



if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root =  [5, 3, 6, 2, 4, None, 7]
    val = 3
    root = buildTreeFromArray(root)
    print(f"Original Tree: {root}")
    print(f"Tree after deleting node with value {val}: {sol.deleteNode(root, val)}")

    # Test 2
    root =   [5, 3, 6, 2, 4, None, 7]
    val = 0
    root = buildTreeFromArray(root)
    print(f"Original Tree: {root}")
    print(f"Tree after deleting node with value {val}: {sol.deleteNode(root, val)}")
