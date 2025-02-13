

def buildTreeFromArray(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = q[front]
        front += 1

        item = arr[index]
        index += 1
        if item is not None:
            node.left = TreeNode(item)
            q.append(node.left)

        if index >= len(arr):
            break

        item = arr[index]
        index += 1
        if item is not None:
            node.right = TreeNode(item)
            q.append(node.right)
    return root

# Top View of BT

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def topView(self, root):
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
