"""
# In Order Traversal
"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def inOrderRecursive(self, root: TreeNode | None):
        # In-order: left subtree, then root, then right subtree
        if root is None:
            return []
        return self.inOrderRecursive(root.left) + [root.value] + self.inOrderRecursive(root.right)

    def inOrderIterative(self, node: TreeNode | None):
        stack = []
        result = []
        while True:
            if node is not None:
                # Go as far left as possible, remembering nodes to visit later
                stack.append(node)
                node = node.left
            elif len(stack) > 0:
                # No more left children, backtrack to the last saved node
                node = stack.pop()
                if node is not None:
                    result.append(node.value)
                    # Now explore its right subtree
                    node = node.right
            else:
                # Stack empty and no current node means traversal is done
                break
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    s = Solution()
    print("===== Recursive In Order Traversal =====")
    print(s.inOrderRecursive(root))
    print("===== Iterative In Order Traversal =====")
    print(s.inOrderIterative(root))
