# Zig Zag or Spiral Traversal

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        leftToRight = True
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if not leftToRight:
                level = level[::-1]
            leftToRight = not leftToRight
            result.append(level)
        return result

    def zigzagLevelOrderOptimized(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        leftToRight = True
        while queue:
            size = len(queue)
            level = [0] * size
            for i in range(size):
                node = queue.popleft()
                # Determine the index to insert the node's value based on the traversal direction
                index = i if leftToRight else (size - 1 - i)
                level[index] = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            leftToRight = not leftToRight
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
    print(s.zigzagLevelOrder(root))
    print(s.zigzagLevelOrderOptimized(root))
