# Count Total odes in a Complete Binary Tree


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    # Function to perform inorder
    # traversal and count nodes
    def inorder(self, root, count):
        # Base case: If the current
        # node is NULL, return
        if root is None:
            return

        # Increment count
        # for the current node
        count[0] += 1

        # Recursively call inorder
        # on the left subtree
        self.inorder(root.left, count)

        # Recursively call inorder
        # on the right subtree
        self.inorder(root.right, count)

    # Function to count nodes in the binary tree
    def count_nodes(self, root):
        # Base case: If the root is NULL,
        # the tree is empty, return 0
        if root is None:
            return 0

        # Initialize count variable to
        # store the number of nodes
        count = [0]

        # Call the inorder traversal
        # function to count nodes
        self.inorder(root, count)

        # Return the final count of
        # nodes in the binary tree
        return count[0]

# Time Complexity: O(logn * logn) | Space Complexity: O(logn)
class Solution2:
    # Function to count nodes
    # in a binary tree
    def count_nodes(self, root):
        # Base case: If the root
        # is NULL, there are no nodes
        if root is None:
            return 0

        # Find the left height and
        # right height of the tree
        lh = self.find_height_left(root)
        rh = self.find_height_right(root)

        # Check if the last level
        # is completely filled
        if lh == rh:
            # If so, use the formula for
            # total nodes in a perfect
            # binary tree i.e. 2^h - 1
            return (1 << lh) - 1

        # If the last level is not completely
        # filled, recursively count nodes in
        # left and right subtrees
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # Function to find the left height of a tree
    def find_height_left(self, node):
        height = 0
        # Traverse left child until
        # reaching the leftmost leaf
        while node:
            height += 1
            node = node.left
        return height

    # Function to find the right height of a tree
    def find_height_right(self, node):
        height = 0
        # Traverse right child until
        # reaching the rightmost leaf
        while node:
            height += 1
            node = node.right
        return height


if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    # Call the count_nodes function
    total_nodes = sol.count_nodes(root)

    # Print the result
    print(f"Total number of nodes in the Complete Binary Tree: {total_nodes}")
