# LCA in BT

from utils import buildTreeFromArray, TreeNode

from collections import deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
            parent_map = {}
            queue = deque([root])
            parent_map[root] = None
            while queue:
                node = queue.popleft()
                if node.left is not None:
                    parent_map[node.left] = node
                    queue.append(node.left)

                if node.right is not None:
                    parent_map[node.right] = node
                    queue.append(node.right)


            queue = deque([target])
            visited = set()
            visited.add(target)
            result = []
            currentDistance = 0

            while queue:
                if currentDistance == k:
                    result.extend(node.val for node in queue)
                    return result
                else:
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
                currentDistance += 1
            return result


if __name__ == "__main__":
    sol1 = Solution()

    # Test Case 1
    root = buildTreeFromArray(  [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4] )
    target = root.left
    k = 2
    # Output: [7, 4, 1]
    print(sol1.distanceK(root, target, k))




    # Test Case 2
    root = buildTreeFromArray([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target = root.left
    k = 2
    # Output: [0, 8]
    print(sol1.distanceK(root, target, k))
