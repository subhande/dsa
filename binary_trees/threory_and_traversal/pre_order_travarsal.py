"""
# Pre Order Traversal
"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def preOrderRecursive(self, root: TreeNode | None):
        if root is None:
            return []
        return [root.value] + self.preOrderRecursive(root.left) + self.preOrderRecursive(root.right)

    def preOrderIterative(self, root: TreeNode | None):
        stack = []
        stack.append(root)
        result = []

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
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
    print(s.preOrderRecursive(root))
    print(s.preOrderIterative(root))
