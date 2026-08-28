# Delete Node and Return Forest

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict, deque


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forests = defaultdict(bool)

        queue = deque([(root, root, None)])  # (node, forestId, parent)

        while queue:
            node, forestId, parent = queue.pop()

            if node.val in to_delete:
                if parent and parent.left == node:
                    parent.left = None
                elif parent and parent.right == node:
                    parent.right = None

                if node.left is not None:
                    queue.append((node.left, node.left, None))

                if node.right is not None:
                    queue.append((node.right, node.right, None))

            else:
                if forestId not in forests:
                    forests[forestId] = True

                if node.left is not None:
                    queue.append((node.left, forestId, node))

                if node.right is not None:
                    queue.append((node.right, forestId, node))

        return list(forests.keys())


class Solution2:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forests = []

        def dfs(node, parent):
            if node is None:
                return
            left = node.left
            right = node.right
            if node.val in to_delete:
                if parent and parent.left == node:
                    parent.left = None
                if parent and parent.right == node:
                    parent.right = None
                if left is not None and left.val not in to_delete:
                    forests.append(left)
                if right is not None and right.val not in to_delete:
                    forests.append(right)

            dfs(node.left, node)
            dfs(node.right, node)

        if root is not None and root.val not in to_delete:
            forests.append(root)

        dfs(root, None)

        return forests


class Solution3:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forests = defaultdict(bool)

        def dfs(node, froestId, parent):
            if node is None:
                return
            left = node.left
            right = node.right
            if node.val in to_delete:
                if parent and parent.left == node:
                    parent.left = None
                if parent and parent.right == node:
                    parent.right = None
                dfs(node.left, node.left, node)
                dfs(node.right, node.right, node)
            else:
                forests[froestId] = True
                dfs(node.left, froestId, node)
                dfs(node.right, froestId, node)

        dfs(root, root, None)

        return list(forests.keys())
