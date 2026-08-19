# Right and Left view of a binary tree

from collections import deque
from typing import List, Optional

from utils import TreeNode, buildTreeFromArray


class Solution1:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def levelOrderTraversal(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    # Time Complexity: O(n) | Space Complexity: O(n)
    def rightSideView(self, root):
        result = []
        if not root:
            return result

        levelOrderTraversal = self.levelOrderTraversal(root)

        for level in levelOrderTraversal:
            result.append(level[-1])

        return result

    # Time Complexity: O(n) | Space Complexity: O(n)
    def leftSideView(self, root):
        result = []
        if not root:
            return result

        levelOrderTraversal = self.levelOrderTraversal(root)

        for level in levelOrderTraversal:
            result.append(level[0])

        return result


class Solution2:
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def rightSideView(self, root):
        result = []
        level = 0
        self.recursionRight(root, level, result)
        return result

    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def leftSideView(self, root):
        result = []
        level = 0
        self.recursionLeft(root, level, result)
        return result

    def recursionRight(self, root, level, result):
        if not root:
            return
        if level == len(result):
            result.append(root.data)
        self.recursionRight(root.right, level + 1, result)
        self.recursionRight(root.left, level + 1, result)

    def recursionLeft(self, root, level, result):
        if not root:
            return
        if level == len(result):
            result.append(root.data)
        self.recursionLeft(root.left, level + 1, result)
        self.recursionLeft(root.right, level + 1, result)


class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        rightSideView = []

        queue = deque([root])

        while queue:
            rightMostNodeValue = None

            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                rightMostNodeValue = node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if rightMostNodeValue is not None:
                rightSideView.append(rightMostNodeValue)

        return rightSideView

    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        leftSideView = []

        queue = deque([root])

        while queue:
            leftMostNodeValue = None

            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if leftMostNodeValue is None:
                    leftMostNodeValue = node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if leftMostNodeValue is not None:
                leftSideView.append(leftMostNodeValue)

        return leftSideView


if __name__ == "__main__":
    sol1 = Solution1()
    sol2 = Solution2()
    # Test Case 1
    root = buildTreeFromArray([1, 2, 3, None, 5, None, 4])
    # Right view: [1, 3, 4]
    # Left view: [1, 2, 5]
    print(sol1.rightSideView(root))
    print(sol1.leftSideView(root))

    print(sol2.rightSideView(root))
    print(sol2.leftSideView(root))

    # Test Case 2
    root = buildTreeFromArray([1, 2, 3, 6, 5, 8, 4])
    # Right view: [1, 3, 4]
    # Left view: [1, 2, 6]
    print(sol1.rightSideView(root))
    print(sol1.leftSideView(root))

    print(sol2.rightSideView(root))
    print(sol2.leftSideView(root))
