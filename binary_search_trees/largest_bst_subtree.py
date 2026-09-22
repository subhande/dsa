# Largest BST Subtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution1: post-order (bottom-up). Each node returns (isBST, size, min, max),
# so every node is visited exactly once.
# Time: O(n) | Space: O(h) recursion stack.
# Empty node returns (True, 0, inf, -inf) so min/max checks need no special cases.
# Invalid subtrees return (False, 0, 0, 0); the dummy values are harmless since
# the parent also requires both children to be valid.
# Note: the node.left/right.val checks and the leaf special case are redundant
# (covered by the min/max checks) and could be removed.
class Solution1:
    def __init__(self):
        self.largestValidBST = 0

    def largestBSTSubtreeHelper(self, node: TreeNode | None) -> tuple:
        # Base Case: If the node is None, return True and size 0
        if node is None:
            return True, 0, float("inf"), float("-inf")

        # Leaf Node is a valid BST of size 1
        if node and node.left is None and node.right is None:
            self.largestValidBST = max(self.largestValidBST, 1)
            return True, 1, node.val, node.val
        # Recursive Case: Check if the left and right subtrees are valid BSTs
        isLeftSubTreeValidBST, leftSubTreeSize, leftMin, leftMax = self.largestBSTSubtreeHelper(node.left)
        # Recursive Case: Check if the left and right subtrees are valid BSTs
        isRightSubTreeValidBST, rightSubTreeSize, rightMin, rightMax = self.largestBSTSubtreeHelper(node.right)

        # Check if the current node is a valid BST
        valid = True
        if node.val <= leftMax or node.val >= rightMin:
            valid = False
        if node.left and node.left.val >= node.val:
            valid = False
        if node.right and node.right.val <= node.val:
            valid = False

        # Update the largest valid BST size if the current node is a valid BST
        if valid and isLeftSubTreeValidBST and isRightSubTreeValidBST:
            self.largestValidBST = max(self.largestValidBST, 1 + leftSubTreeSize + rightSubTreeSize)
        else:
            self.largestValidBST = max(self.largestValidBST, max(leftSubTreeSize, rightSubTreeSize))
            
        # Return the size of the largest valid BST subtree rooted at the current node
        if valid and isLeftSubTreeValidBST and isRightSubTreeValidBST:
            return True, 1 + leftSubTreeSize + rightSubTreeSize, min(leftMin, node.val), max(rightMax, node.val)
        return False, 0, 0, 0

    def largestBSTSubtree(self, root: TreeNode | None) -> int:

        if root is None:
            return 0
        
        self.largestBSTSubtreeHelper(root)

        return self.largestValidBST


# Solution2: top-down brute force. At each node, validate the whole subtree via
# in-order traversal, then count nodes if valid; otherwise recurse into children.
# Time: best O(n) (whole tree is a BST), balanced O(n log n),
#       worst O(n^2) (skewed tree with a violation near the bottom).
# Space: O(h). Simpler, but stateful (self.previous is reset per call).
# Solution1 is the more optimized approach.
class Solution2:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """Check if given tree is a valid BST using in-order traversal."""
        # An empty tree is a valid Binary Search Tree.
        if not root:
            return True
        
        # If left subtree is not a valid BST return false.
        if not self.is_valid_bst(root.left):
            return False

        # If current node's value is not greater than the previous 
        # node's value in the in-order traversal return false.
        if self.previous and self.previous.val >= root.val:
            return False

        # Update previous node to current node.
        self.previous = root

        # If right subtree is not a valid BST return false.
        return self.is_valid_bst(root.right)

    # Count nodes in current tree.
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        # Add nodes in left and right subtree.
        # Add 1 and return total size.
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Previous node is initially null.
        self.previous = None

        # If current subtree is a validBST, its children will have smaller size BST.
        if self.is_valid_bst(root):
            return self.count_nodes(root)
        
        # Find BST in left and right subtrees of current nodes.
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))