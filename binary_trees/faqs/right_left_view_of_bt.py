# Right and Left view of a binary tree

from utils import buildTreeFromArray, TreeNode

from collections import deque


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
