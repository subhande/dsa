# Amount of Time for Binary Tree to Be Infected


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {}
        queue = deque([root])
        parent_map[root] = None
        targetNode = None

        while queue:
            node = queue.popleft()

            if node.val == start:
                targetNode = node

            if node.left is not None:
                queue.append(node.left)
                parent_map[node.left] = node

            if node.right is not None:
                queue.append(node.right)
                parent_map[node.right] = node

        queue = deque([targetNode])
        visited = set()
        visited.add(targetNode)
        currentTime = -1

        while queue:

            size = len(queue)
            for _ in range(size):

                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                if parent_map[node] and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])

            currentTime += 1
        return currentTime
