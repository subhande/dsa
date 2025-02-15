import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray

# BST iterator

# ------------------------------------------------------------------------------
# BSTIterator:
#
# This iterator computes an in-order traversal (sorted order for BST) by
# visiting every node and storing its value.
#
# Time Complexities:
#   • Initialization (__init__ and inOrder):
#         O(n) total, where n is the total number of nodes; it visits every node.
#   • next:
#         O(1) per call, as it advances an index in a precomputed list.
#   • hasNext:
#         O(1)
#
# Space Complexity:
#   O(n) since it stores the values of all n nodes from the tree.
# ------------------------------------------------------------------------------
class BSTIterator:
    def __init__(self, root):
        # List to store the in-order traversal of the BST.
        self.values = []
        # Index pointer to traverse the in-order list; initialized to -1.
        self.index = -1
        # Perform the in-order traversal once at initialization.
        self.inOrder(root)  # O(n) time and space.

    def inOrder(self, root):
        """Recursive function to do an in-order traversal of the tree."""
        if root:
            self.inOrder(root.left)   # Recurse on the left child.
            self.values.append(root.data)  # Process current node; O(1) time.
            self.inOrder(root.right)  # Recurse on the right child.

    def hasNext(self):
        """Return True if there are more nodes to process in the in-order list."""
        # O(1) time: just checks if index + 1 is within bounds.
        return self.index + 1 < len(self.values)

    def next(self):
        """Move pointer to next element and return its value."""
        # Increment index to point to the next element.
        self.index += 1
        # O(1) time: returns the current element.
        return self.values[self.index]
# ------------------------------------------------------------------------------
# BSTIteratorOptimized:
#
# This iterator uses a stack to simulate the controlled recursion for an
# in-order traversal. It only stores nodes that are yet to be processed,
# which is at most O(h) where h is the height of the tree.
#
# Time Complexities:
#   • Initialization (__init__ and pushLeft):
#         O(h) where h is the tree height (in worst-case, h = n for a skewed tree).
#   • next:
#         Amortized O(1) per call. Although a single next() may process O(h) nodes
#         (if a node with a right child is encountered), over the entire traversal,
#         each node is pushed and popped exactly once.
#   • hasNext:
#         O(1) time.
#
# Space Complexity:
#   O(h) space for the stack.
# ------------------------------------------------------------------------------
class BSTIteratorOptimized:
    def __init__(self, root):
        # Stack to store the nodes along the leftmost path of the tree.
        self.stack = []
        # Initialize the stack with all the left-most nodes from the root.
        self.pushLeft(root)  # Starts with O(h) time and space.

    def pushLeft(self, root):
        """Push all the left children of the given node onto the stack."""
        while root:
            # O(1) time per push; runs O(h) times at most.
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """Return True if there is at least one node left in the stack."""
        # O(1) time: checks if the stack is non-empty.
        return len(self.stack) > 0

    def next(self):
        """
        Process and return the next smallest value:
          - Pop a node from the stack (O(1) time).
          - If the node has a right child, traverse its left-most branch.
        """
        # Retrieve the next node in in-order sequence.
        node = self.stack.pop()
        # If the node has a right child, push all of its left descendants.
        self.pushLeft(node.right)
        return node.data  # Return the node's value.


if __name__ == "__main__":
    # Example:
    #      5
    #     / \
    #    3   6
    #   / \   \
    #  2   4   7
    root = buildTreeFromArray([5, 3, 6, 2, 4, None, 7])
    # Initialize the BSTIterator with the root.
    bstIterator = BSTIterator(root)
    # Initialize the BSTIteratorOptimized with the root.
    bstIteratorOptimized = BSTIteratorOptimized(root)

    # Test the BSTIterator.
    print("BSTIterator:")
    while bstIterator.hasNext():
        print(bstIterator.next(), end=" ")  # 2 3 4 5 6 7
    print()

    # Test the BSTIteratorOptimized.
    print("BSTIteratorOptimized:")
    while bstIteratorOptimized.hasNext():
        print(bstIteratorOptimized.next(), end=" ")  # 2 3 4 5 6 7
    print()
