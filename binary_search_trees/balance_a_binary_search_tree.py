# Balance a Binary Search Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def balanceBST(self, root):
        nodes = []

        # Step 1: Get sorted values using inorder traversal
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build a balanced BST from sorted array
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nodes[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(nodes) - 1)
