# LCA in BT

from utils import buildTreeFromArray, TreeNode

from collections import deque



class Solution1:
    def levelOrderTraversalWithNulls(self, root):
        if root is None:
            return []

        q = deque()
        q.append(root)
        levelOrder = []
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node is None:
                    level.append(node)
                    q.append(None)
                    q.append(None)
                else:
                    level.append(node.data)
                    q.append(node.left)
                    q.append(node.right)
            if level.count(None) == len(level):
                break
            levelOrder.append(level)
        return levelOrder

    def widthOfBinaryTree(self, root):
        levelOrderTraversal = self.levelOrderTraversalWithNulls(root)
        maxWidth = 0
        for level in levelOrderTraversal:
            # Trim the None values from the left and right
            left = 0
            right = len(level) - 1
            while level[left] is None:
                left += 1
            while level[right] is None:
                right -= 1
            maxWidth = max(maxWidth, right - left + 1)
        return maxWidth


class Solution2:
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        maxWidth = 0
        q = deque()
        q.append((root, 0))
        while q:
            level = []
            size = len(q)
            start, end = 0, 0
            # Get the index of the first node in the level
            min_level_index = q[0][1]
            for i in range(size):
                node, index = q.popleft()
                # Normalize the index relative to the first node in the level | This is optional
                index -= min_level_index
                if i == 0:
                    start = index
                if i == size - 1:
                    end = index
                level.append((node.data, index))
                if node.left is not None:
                    q.append((node.left, 2 * index + 1))
                if node.right is not None:
                    q.append((node.right, 2 * index + 2))
            maxWidth = max(maxWidth, end - start + 1)
        return maxWidth


if __name__ == "__main__":
    sol1 = Solution1()
    sol2 = Solution2()

    # Test Case 1
    root = buildTreeFromArray( [1, 3, 2, 5, 3, None, 9])
    # Output: 4
    print(sol1.widthOfBinaryTree(root))
    print(sol2.widthOfBinaryTree(root))



    # Test Case 2
    root = buildTreeFromArray([1, 3, 2, 5, None, None, 9, 6, None, 7])
    # Output: 7
    print(sol1.widthOfBinaryTree(root))
    print(sol2.widthOfBinaryTree(root))
