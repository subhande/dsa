# Construct BST from Preorder Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: Recursive Brute Force
# Time Complexity: O(n^2) | Space Complexity: O(n)
class Solution:
    def bstFromPreorderhelper(self, preorder: list[int], start: int, end: int):
        if end < start or start == -1 or end == -1:
            return None

        leftSubtreeEnd = end
        rightSubtreeStart = end + 1

        for index in list(range(start + 1, end + 1)):
            if preorder[start] < preorder[index]:
                leftSubtreeEnd = index - 1
                rightSubtreeStart = index
                break

        node = TreeNode(preorder[start])
        node.left = self.bstFromPreorderhelper(preorder, start + 1, leftSubtreeEnd)
        node.right = self.bstFromPreorderhelper(preorder, rightSubtreeStart, end)

        return node

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:

        return self.bstFromPreorderhelper(preorder, 0, len(preorder) - 1)


# Approach 2: Recursive with preorder and inorder traversal
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(preorder)):
            nonlocal pre_idx
            # If there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            p
            # build the left subtree
            root.left = helper(in_left, index)
            # build the right subtree
            root.right = helper(index + 1, in_right)
            return root

        inorder = sorted(preorder)
        # start from the first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


# Approach 3: Recursive with bounds
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower=float("-inf"), upper=float("inf")):
            nonlocal idx
            # If all elements from preorder are used
            # Then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # If the current element
            # couldn't be placed here to meet BST requirements
            if val < lower or val > upper:
                return None

            # place the current element
            # and recursively construct subtrees
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()
