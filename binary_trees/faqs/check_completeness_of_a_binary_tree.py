# Check Completeness Of a Binary Tree



from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        queue = deque([root])
        level = 0
        while queue:
            size = len(queue)
            allNodesPresent = size == (2 ** level)
            rightChildMisssing = False
            noChild = False
            for _ in range(len(queue)):
                node = queue.popleft()

                if (node.left is None and node.right is not None):
                    return False
                if rightChildMisssing is True and (node.left is not None or node.right is not None):
                    return False
                if noChild is True and (node.left is not None or node.right is not None):
                    return False
                if node.left is None and node.right is None:
                    noChild = True
                if node.left is not None and node.right is None:
                    rightChildMisssing = True

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            if allNodesPresent is False and len(queue) > 0:
                return False
            level += 1

        return True


class Solution2:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        queue = deque([root])
        nullNodeFound = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    nullNodeFound = True
                    continue
                else:
                    if nullNodeFound:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)

        return True
