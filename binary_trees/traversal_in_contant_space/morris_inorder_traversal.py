

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# This method performs an inorder traversal of a binary tree
# using the Morris Traversal algorithm, which does not use
# additional space for a stack or recursion.

class Solution:
    def getInorder(self, root):
        # List to store inorder traversal
        inorder = []
        # Pointer to current node
        cur = root

        while cur is not None:
            if cur.left is None:
                # Add current node's value and move to right child
                inorder.append(cur.data)
                cur = cur.right
            else:
                # Find predecessor
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                if prev.right is None:
                    # Establish temporary link
                    prev.right = cur
                    # Move to left child
                    cur = cur.left
                else:
                    # Remove temporary link
                    # Add current node's value
                    # Move to right child
                    prev.right = None
                    inorder.append(cur.data)
                    cur = cur.right

        # Return inorder traversal
        return inorder

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    sol = Solution()
    inorder = sol.getInorder(root)

    print("Binary Tree Morris Inorder Traversal:", end=" ")
    for val in inorder:
        print(val, end=" ")
    print()
