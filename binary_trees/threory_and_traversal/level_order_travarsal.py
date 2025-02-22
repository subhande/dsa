"""
# Level Order Traversal
"""

from collections import deque

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None):
        result = []
        if root is None:
            return result
        queue = deque()

        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
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
    print(s.levelOrder(root))
