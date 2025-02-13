# Top View of BT

from utils import buildTreeFromArray, TreeNode

from collections import deque

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def topView(self, root: TreeNode | None):
        if not root:
            return []

        # Dictionary to store nodes in each column
        top_view = dict()
        # Queue to perform BFS (node, column index, row index)
        queue = deque([(root, 0)])

        while queue:
            node, line = queue.popleft()

            if line not in top_view:
                top_view[line] = node.data

            # Traverse left subtree, move column left (-1)
            if node.left:
                queue.append((node.left, line - 1))
            # Traverse right subtree, move column right (+1)
            if node.right:
                queue.append((node.right, line + 1))

        return [top_view[line] for line in sorted(top_view.keys())]


if __name__ == "__main__":

    sol = Solution()

    # Test Case 1
    root = buildTreeFromArray([20, 8, 22, 5, 3, None, 25, None, None, 10 ,14])
    # Bottom view: [2, 1, 3, 5]
    print(sol.topView(root))
