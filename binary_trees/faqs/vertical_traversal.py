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

# Vertical Order Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

from collections import defaultdict, deque

class Solution1:
    # Time Complexity: O(n) * O(log n) *  O(log n) * O(log n) = O(nlogn) | Space Complexity: O(n)
    def verticalTraversal(self, root):
        """
        Perform vertical order traversal of a binary tree.

        :param root: TreeNode - The root of the binary tree.
        :return: List[List[int]] - A list of lists containing the vertical order traversal.
        """

        if not root:
            return []

        # Dictionary to store the nodes at each vertical distance and level.
        # nodes_map[x][y] will hold a list of nodes at vertical distance x and level y.
        nodes_map = defaultdict(lambda: defaultdict(list))

        # Queue for BFS traversal (stores node along with its x and y coordinates)
        queue = deque([(root, 0, 0)])  # (node, x, y)

        # Perform BFS to populate nodes_map with nodes at each (x, y) coordinate.
        while queue:
            node, x, y = queue.popleft()

            # Add the node's value to the map at the correct x and y
            nodes_map[x][y].append(node.data)

            # Add the left child with updated coordinates to the queue
            if node.left:
                queue.append((node.left, x - 1, y + 1))

            # Add the right child with updated coordinates to the queue
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        # Prepare the result by sorting keys and compiling nodes
        result = []
        for x in sorted(nodes_map):
            column = []
            for y in sorted(nodes_map[x]):
                # Sort the nodes at the same position to maintain the order
                column.extend(sorted(nodes_map[x][y]))
            result.append(column)

        return result


class Solution2:
    # Time Complexity: O(n) * O(log n) * O(log n) = O(nlogn) | Space Complexity: O(n)
    def verticalTraversal(self, root):
        if not root:
            return []

        # Dictionary to store nodes in each column
        column_table = defaultdict(list)
        # Queue to perform BFS (node, column index, row index)
        queue = deque([(root, 0, 0)])

        while queue:
            node, column, row = queue.popleft()
            column_table[column].append((row, node.data))

            # Traverse left subtree, move column left (-1) and row down (+1)
            if node.left:
                queue.append((node.left, column - 1, row + 1))
            # Traverse right subtree, move column right (+1) and row down (+1)
            if node.right:
                queue.append((node.right, column + 1, row + 1))

        # Sort by column index
        sorted_columns = sorted(column_table.keys())

        result = []
        for col in sorted_columns:
            # Sort nodes first by row index, then by value
            column_table[col].sort()
            result.append([val for _, val in column_table[col]])

        return result


if __name__ == "__main__":

    sol1 = Solution1()
    sol2 = Solution2()
    tree = [3, 9, 20, None, None, 15, 7]
    root = buildTreeFromArray(tree)
    expected = [[9], [3, 15], [20], [7]]
    print(sol1.verticalTraversal(root))
    print(sol2.verticalTraversal(root))

    tree = [1, 2, 3, 4, 5, 6, 7]
    expected = [[4], [2], [1, 5, 6], [3], [7]]
    root = buildTreeFromArray(tree)
    print(sol1.verticalTraversal(root))
    print(sol2.verticalTraversal(root))
