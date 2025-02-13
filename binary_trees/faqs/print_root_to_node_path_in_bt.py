# Print root to node path in BT

from utils import buildTreeFromArray, TreeNode

from collections import deque


class Solution:
    def dfs(self, node, currPath, allPaths):
        if node is None:
            return
        currPath.append(node.data)

        if node.left is None and node.right is None:
            allPaths.append(currPath)

        self.dfs(node.left, currPath[:], allPaths)
        self.dfs(node.right, currPath[:], allPaths)

        return

    # Time Complexity: O(n)
    # Axillary Space Complexity: O(h) where h is the height of the tree
    # Output Space Complexity: O(nh) as we have n/2 leaf nodes and each leaf node has height h
    def allRootToLeaf(self, root):
        allPaths = []
        self.dfs(root, [], allPaths)
        return allPaths


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    root = buildTreeFromArray( [1, 2, 3, None, 5, None, 4])
    # Right view: [1, 3, 4]
    # Left view: [1, 2, 5]
    print(sol.allRootToLeaf(root))



    # Test Case 2
    root = buildTreeFromArray([1, 2, 3, 6, 5, 8, 4])
    # Right view: [1, 3, 4]
    # Left view: [1, 2, 6]
    print(sol.allRootToLeaf(root))
