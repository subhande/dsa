from typing import List

# Note: Here DFS is better than BFS because we can keep track of the current path and its sum as we traverse down the tree. In BFS, we would need to store all paths at each level, which can be less efficient in terms of space.


# Time Complexity: O(n * h)
# - Skewed tree: O(n^2)
# - Balanced tree: O(n * log(n))
# Space Complexity: O(h²) auxiliary
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, currentPath, curentPathSum, validPaths, targetSum):
        currentPath.append(node.val)
        curentPathSum += node.val
        if curentPathSum == targetSum and node.left is None and node.right is None:
            validPaths.append(currentPath)
        if node.left is not None:
            self.dfs(node.left, currentPath[:], curentPathSum, validPaths, targetSum)
        if node.right is not None:
            self.dfs(node.right, currentPath[:], curentPathSum, validPaths, targetSum)

    def pathSum(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        currentPath = []
        curentPathSum = 0
        validPaths = []
        self.dfs(root, currentPath, curentPathSum, validPaths, targetSum)
        return validPaths


# Time Complexity: O(n * h) | Worst case: O(n^2)
# Space Complexity: O(h) auxiliary
class Solution2:
    def dfs(self, node, currentPath, curentPathSum, validPaths, targetSum):
        currentPath.append(node.val)
        curentPathSum += node.val
        if curentPathSum == targetSum and node.left is None and node.right is None:
            validPaths.append(currentPath[:])
        if node.left is not None:
            self.dfs(node.left, currentPath, curentPathSum, validPaths, targetSum)
        if node.right is not None:
            self.dfs(node.right, currentPath, curentPathSum, validPaths, targetSum)
        currentPath.pop()

    def pathSum(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        currentPath = []
        curentPathSum = 0
        validPaths = []
        self.dfs(root, currentPath, curentPathSum, validPaths, targetSum)
        return validPaths


# Time Complexity: O(n * h) | Worst case: O(n^2)
class Solution3:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        currentPath = []
        curentPathSum = 0
        validPaths = []
        stack = [(root, currentPath, curentPathSum)]

        while stack:
            node, currentPath, curentPathSum = stack.pop()
            currentPath.append(node.val)
            curentPathSum += node.val

            if curentPathSum == targetSum and node.left is None and node.right is None:
                validPaths.append(currentPath[:])

            if node.right is not None:
                stack.append((node.right, currentPath[:], curentPathSum))
            if node.left is not None:
                stack.append((node.left, currentPath[:], curentPathSum))
