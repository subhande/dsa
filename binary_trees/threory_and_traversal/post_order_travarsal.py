
"""
# Post Order Traversal
"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

class Solution:
    def postOrderRecursive(self, root: TreeNode | None):
        if root is None:
            return []
        return self.postOrderRecursive(root.left) + self.postOrderRecursive(root.right) + [root.value]

    def postOrderIterative(self, root: TreeNode | None):
        stack = []
        result = []
        if root is None:
            return result

        current = root
        prev = None

        while current is not None or stack:
            while current is not None:
                # Push the current node to the stack
                stack.append(current)
                # Move to the left child
                current = current.left
            # Set current to the top of the stack
            current = stack[-1]
            print(stack)
            # If the right child is None or already visited
            if current.right is None or current.right == prev:
                # Append the current node to the result
                result.append(current.value)
                # Pop the current node from the stack
                stack.pop()
                # Set prev to the current node
                prev = current
                # Set current to None
                current = None
            else:
                # Move to the right child
                current = current.right
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
    print(s.postOrderRecursive(root))
    print(s.postOrderIterative(root))
