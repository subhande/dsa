import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)




from binary_search_trees.utils import TreeNode, buildTreeFromArray

from typing import Optional
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution2:
    def find(self, root: Optional[TreeNode], k: int, seen: set) -> bool:
        if root is None:
            return False
        if k - root.val in seen:
            return True
        seen.add(root.val)
        return self.find(root.left, k, seen) or self.find(root.right, k, seen)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        return self.find(root, k, seen)

# BST Iterator to iterate in the inorder and reverse inorder manner
class BSTIterator:
    def __init__(self, root, is_reverse):
        self.stack = []
        self.reverse = is_reverse
        self.pushAll(root)

    # Helper function to push all left or right nodes
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left

    # Check if there are more elements in the BST
    def hasNext(self):
        return len(self.stack) > 0

    # Get the next element in the inorder or reverse inorder traversal
    def next(self):
        node = self.stack.pop()
        if not self.reverse:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return node.data

# Two sum in BST
class Solution:
    # Inorder traversal to obtain a sorted list of values.
        # Time: O(n) where n is the number of nodes.
        # Space: O(n) for the recursion call stack (worst-case) and the list of values.
        def inOrder(self, root, values):
            if root:
                self.inOrder(root.left, values)
                values.append(root.data)  # Note: Here we assume 'val' is the attribute of TreeNode.
                self.inOrder(root.right, values)

        # Approach 1:
        # Do an inorder traversal to create a sorted array of node values,
        # then use the two-pointer technique to check for the target sum.
        #
        # Time Complexity: O(n) - one full traversal for collecting values
        #                          + O(n) for the two-pointer scan.
        # Space Complexity: O(n) - for the sorted values array.
        def twoSumBST(self, root, k):
            values = []
            self.inOrder(root, values)
            i, j = 0, len(values) - 1
            while i < j:
                current_sum = values[i] + values[j]
                if current_sum == k:
                    return True
                elif current_sum < k:
                    i += 1
                else:
                    j -= 1
            return False

        # Approach 2 (Optimized):
        # Use two BST iterators, one that iterates in normal inorder (smallest first)
        # and one in reverse inorder (largest first), then use a two-pointer technique
        # without needing extra space to store all nodes.
        #
        # Time Complexity: O(n) in worst-case where we may have to traverse all nodes.
        #                    Average operation of next() is constant, but may cost O(h).
        # Space Complexity: O(h) where h is the height of the tree due to stacks
        #                    used by both iterators. (In worst-case, h = n)
        def twoSumBSTOptimized(self, root, k):
            leftIterator = BSTIterator(root, False)  # normal inorder iterator
            rightIterator = BSTIterator(root, True)  # reverse inorder iterator

            # Initialize two pointers.
            left = leftIterator.next()  # smallest element
            right = rightIterator.next()  # largest element

            while left < right:
                current_sum = left + right
                if current_sum == k:
                    return True
                elif current_sum < k:
                    # Move left pointer to next greater value.
                    left = leftIterator.next() if leftIterator.hasNext() else left
                else:
                    # Move right pointer to next smaller value.
                    right = rightIterator.next() if rightIterator.hasNext() else right
            return False


if __name__ == "__main__":
    sol = Solution()
    root = buildTreeFromArray([5,3,6,2,4,None,7])
    k = 9
    print(sol.twoSumBST(root, k))  # True
    print(sol.twoSumBSTOptimized(root, k))  # True

    root = buildTreeFromArray([5,3,6,2,4,None,7])
    k = 14
    print(sol.twoSumBST(root, k))  # False
    print(sol.twoSumBSTOptimized(root, k))  # False
