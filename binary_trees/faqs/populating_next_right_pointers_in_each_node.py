# Populating Next Right Pointers in Each Node

from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        if root is None:
            return

        queue = deque([(root, 0)])

        while queue:
            size = len(queue)

            for _ in range(size):
                node, row = queue.popleft()

                if len(queue) > 0 and queue[0][-1] == row:
                    node.next = queue[0][0]

                if node.left is not None:
                    queue.append((node.left, row + 1))

                if node.right is not None:
                    queue.append((node.right, row + 1))

        return root


class Solution2:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        if root is None:
            return

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return root
