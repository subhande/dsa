import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


# Correct a BST with two nodes swapped


class Solution:
    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root.data] + self.inOrder(root.right)

    # Time complexity: O(n) | Space complexity: O(h) for the recursive call stack
    def recoverTree(self, root: TreeNode) -> TreeNode:
        # Initialize pointers for first, second, and previous node in inorder traversal.
        first = second = prev = None

        # Helper function: perform recursive inorder traversal
        def inorder(node: TreeNode):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)

            # Check for swapped nodes: the previous node should not be greater than the current node.
            if prev and prev.data > node.data:
                # For the first occurrence, record prev as "first"
                if not first:
                    first = prev
                # For both first and subsequent occurrences, update "second" as current
                second = node

            prev = node  # update previous node to current
            inorder(node.right)

        # Perform the inorder traversal to find the two nodes:
        inorder(root)

        # Swap the values of the two nodes, if they have been identified.
        if first and second:
            first.data, second.data = second.data, first.data

        # Return the root of the corrected BST.
        return root

    # Time complexity: O(n) | Space complexity: O(h) for the stack
    def recoverTreeIterative(self, root: TreeNode) -> TreeNode:
        # Initialize pointers for first, second, and previous node in inorder traversal.
        first = second = prev = None

        # Initialize a stack for iterative inorder traversal.
        stack = []

        # Start with the root node.
        node = root

        # Iterate through the tree until the stack is empty and the current node is None.
        while stack or node:
            # Traverse left as far as possible, pushing nodes onto the stack.
            while node:
                stack.append(node)
                node = node.left

            # Pop the top node from the stack.
            node = stack.pop()

            # Check for swapped nodes: the previous node should not be greater than the current node.
            if prev and prev.data > node.data:
                # For the first occurrence, record prev as "first"
                if not first:
                    first = prev
                # For both first and subsequent occurrences, update "second" as current
                second = node

            prev = node

            # Move to the right child of the current node.
            node = node.right

        # Swap the values of the two nodes, if they have been identified.
        if first and second:
            first.data, second.data = second.data, first.data

        # Return the root of the corrected BST.
        return root


if __name__ == "__main__":
    sol = Solution()

    # Test case 1:
    root = buildTreeFromArray([1, 3, None, None, 2])
    print(f"Original tree: {root} | Inorder: {sol.inOrder(root)}")
    print(f"Corrected tree: {sol.recoverTree(root)} | Inorder: {sol.inOrder(root)}")
    root = buildTreeFromArray([1, 3, None, None, 2])
    print(f"Original tree: {root} | Inorder: {sol.inOrder(root)}")
    print(f"Corrected tree: {sol.recoverTreeIterative(root)} | Inorder: {sol.inOrder(root)}")

    # Test case 2:
    root = buildTreeFromArray([3, 1, 4, None, None, 2])
    print(f"Original tree: {root} | Inorder: {sol.inOrder(root)}")
    print(f"Corrected tree: {sol.recoverTree(root)} | Inorder: {sol.inOrder(root)}")
    root = buildTreeFromArray([3, 1, 4, None, None, 2])
    print(f"Original tree: {root} | Inorder: {sol.inOrder(root)}")
    print(f"Corrected tree: {sol.recoverTreeIterative(root)} | Inorder: {sol.inOrder(root)}")
