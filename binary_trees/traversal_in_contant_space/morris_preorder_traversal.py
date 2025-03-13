


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        # List to store the preorder traversal result
        preorder = []

        # Pointer to the current node, starting with the root
        cur = root

        # Iterate until the current node becomes None
        while cur:
            # If the current node has no left child
            # Add the value of the current node to the preorder list
            if not cur.left:
                preorder.append(cur.data)
                # Move to the right child
                cur = cur.right
            else:
            # If the current node has a left child
            # Create a pointer to traverse to the rightmost node in the left subtree
                prev = cur.left

            # Traverse to the rightmost node in the left subtree
            # or until we find a node whose right child is not yet processed
                while prev.right and prev.right != cur:
                    prev = prev.right

            # If the right child of the rightmost node is null
            # Set the right child of the rightmost node to the current node
            # Add the value of the current node to the preorder list and
            # move to the left child

                if not prev.right:
                    prev.right = cur
                    preorder.append(cur.data)
                    cur = cur.left

            # If the right child of the rightmost node is not null
            # Reset the right child to null
                else:
                    prev.right = None
                    cur = cur.right

        # Return the resulting preorder traversal list
        return preorder

# Example usage:
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(2)

sol = Solution()
preorder = sol.preorder(root)
print("Binary Tree Morris Preorder Traversal: ", preorder)
