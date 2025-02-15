import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
from tkinter.constants import LEFT
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray

# Construct a BST from a preorder traversal

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

    # Time Complexity: O(nh) | Space Complexity: O(h)
    def bstFromPreorderRecursive(self, preorder):
        root = TreeNode(preorder[0])
        for ele in preorder[1:]:
            self.insertIntoBSTRecrsive(root, ele)
        return root

    # Time Complexity: O(nlogn + n) | Space Complexity: O(n)
    def bstFromPreorderUsingInorder(self, preorder):
        inorder = sorted(preorder)
        # Create a map to store indices
        # of elements in the inorder traversal
        inorderMap = {val: idx for idx, val in enumerate(inorder) }

        # Recursive helper function to build the tree
        def helper(preStart, preEnd, inStart, inEnd):
            # Base case
            if preStart > preEnd or inStart > inEnd:
                return None

            # The first element in the preorder traversal is the root
            root = TreeNode(preorder[preStart])

            # Find the index of the root in the inorder traversal
            rootIdx = inorderMap[root.data]

            # Calculate the number of elements in the left subtree
            leftSubtreeSize = rootIdx - inStart

            # Recursively build the left and right subtrees
            root.left = helper(preStart + 1, preStart + leftSubtreeSize, inStart, rootIdx - 1)
            root.right = helper(preStart + leftSubtreeSize + 1, preEnd, rootIdx + 1, inEnd)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


    # Time Complexity: O(n) | Space Complexity: O(n)
    # The time complexity is O(n) because each node is processed once, and even in the worst case, the total number of stack operations (push and pop) is at most n.
    # The space complexity is O(n) in the worst case when the tree is skewed, as the stack may hold up to n nodes.
    def bstFromPreorderIterative(self, preorder):
            if not preorder:
                return None

            # The first element is the root
            root = TreeNode(preorder[0])
            stack = [root]

            # Iterate over the rest of the preorder sequence
            for value in preorder[1:]:
                node = TreeNode(value)

                # If the current value is less than the last node's value on the stack,
                # it belongs as a left child.
                if value < stack[-1].data:
                    stack[-1].left = node
                    stack.append(node)
                else:
                    # Otherwise, pop nodes until finding the parent under which the new node
                    # should be attached as a right child.
                    last = None
                    while stack and stack[-1].data < value:
                        last = stack.pop()
                    if last:
                        last.right = node
                    stack.append(node)
            return root

    def bstFromPreorderOptimalHelper(self, preorder, bound, index):
        # If all elements are used or the next element
        # is greater than the bound, return None
        if index[0] == len(preorder) or preorder[index[0]] > bound:
            return None

        # Create a new TreeNode with the current value
        root = TreeNode(preorder[index[0]])
        index[0] += 1

        # Recursively construct the left subtree
        # with the current value as the new bound
        root.left = self.bstFromPreorderOptimalHelper(preorder, root.data, index)

        # Recursively construct the right subtree
        # with the same bound as the parent's bound
        root.right = self.bstFromPreorderOptimalHelper(preorder, bound, index)

        # Return the constructed subtree's root
        return root

    # Time Complexity: O(n) | Space Complexity: O(h)
    def bstFromPreorderOptimal(self, preorder):
        # Start the recursive function
        # with the first element as the root
        # and the entire range of valid numbers
        return self.bstFromPreorderOptimalHelper(preorder, float('inf'), [0])



if __name__ == "__main__":
    sol = Solution()

    # Test 1
    preorder = [8, 5, 1, 7, 10, 12]
    print(sol.bstFromPreorderRecursive(preorder)) # [8, 5, 10, 1, 7, None, 12]
    print(sol.bstFromPreorderUsingInorder(preorder)) # [8, 5, 10, 1, 7, None, 12]
    print(sol.bstFromPreorderIterative(preorder)) # [8, 5, 10, 1, 7, None, 12]
    print(sol.bstFromPreorderOptimal(preorder)) # [8, 5, 10, 1, 7, None, 12]

    # Test 2
    preorder = [1, 3]
    print(sol.bstFromPreorderRecursive(preorder)) # [1, None, 3]
    print(sol.bstFromPreorderUsingInorder(preorder)) # [1, None, 3]
    print(sol.bstFromPreorderIterative(preorder)) # [1, None, 3]
    print(sol.bstFromPreorderOptimal(preorder)) # [1, None, 3]
