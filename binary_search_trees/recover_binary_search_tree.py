# Recover Binary Search Tree
# https://www.youtube.com/watch?v=ZWGW7FminDM


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Brute Force: Inorder Traversal and Sorting
# Time Complexity: O(nlogn) | Space Complexity: O(n)
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        nodes = []
        invalidNode = None

        # Step 1: Get sorted values using inorder traversal
        def inorder(node):
            nonlocal invalidNode
            if not node:
                return

            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        nodes.sort()

        index = 0

        def recover(node):
            nonlocal index
            if node is None:
                return
            recover(node.left)
            node.val = nodes[index]
            index += 1
            recover(node.right)

        recover(root)


# Approach 2: Inorder Traversal and Swapping
# Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return

            inorder(node.left)

            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val


# Approach 2
# Case 1: Swapped nodes are not adjacent
# Example: 3, |25|, 7, 8, 10, 15, 20, |5|
# Case 2: Swapped nodes are adjacent
# Example: 3, 5, 8, |7|, 10, 15, 20, 25


class Solution2:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Initialize pointers for the two nodes to be swapped and the previous node
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return

            inorder(node.left)

            # Check for the first and second nodes that are out of order
            if prev and node.val < prev.val:
                # If this is the first time we encounter an out-of-order pair, mark 'first' as 'prev'
                if not first:
                    first = prev
                # Always mark 'second' as the current node, as it may be the second out-of-order node
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        if first and second:
            # Swap the values of the two nodes to recover the BST
            first.val, second.val = second.val, first.val
