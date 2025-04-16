# Delete Node and Return Forest

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forests = defaultdict(bool)

        queue = deque([(root, root, None)])



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
