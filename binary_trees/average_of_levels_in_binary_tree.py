# Average of Levels in Binary Tree
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevelsRecursiveHelper(self, node: Optional[TreeNode], level: int, levels: dict):
        if node is None:
            return

        levels[level].append(node.val)

        self.averageOfLevelsRecursiveHelper(node.left, level + 1, levels)
        self.averageOfLevelsRecursiveHelper(node.right, level + 1, levels)

    def averageOfLevelsRecursive(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(list)
        self.averageOfLevelsRecursiveHelper(root, 0, levels)

        levelAvg = []
        for level, values in levels.items():
            levelAvg.append(sum(values) / len(values))
        return levelAvg

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = 0
        queue = deque()

        queue.append((root, 0))

        levels = defaultdict(list)

        while queue:
            node, level = queue.popleft()

            levels[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        levelAvg = []
        for level, values in levels.items():
            levelAvg.append(sum(values) / len(values))
        return levelAvg

    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            result.append(sum(level) / len(level))
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.averageOfLevels(root))
