# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePathsHelper(self, node: TreeNode | None, currPath: str, paths: list[str]) -> None:
        if node is None:
            return
        currPath += str(node.val) if not currPath else f"->{node.val}"
        if node.left is None and node.right is None:
            paths.append(currPath)
            return
        if node.left is not None:
            self.binaryTreePathsHelper(node.left, currPath, paths)
        if node.right is not None:
            self.binaryTreePathsHelper(node.right, currPath, paths)
        return

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root is None:
            return []
        paths = []
        self.binaryTreePathsHelper(root, "", paths)
        return paths


class Solution2:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root is None:
            return []
        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, currPath = stack.pop()
            if node.left is None and node.right is None:
                paths.append(currPath)
            if node.right is not None:
                stack.append((node.right, f"{currPath}->{node.right.val}"))
            if node.left is not None:
                stack.append((node.left, f"{currPath}->{node.left.val}"))
        return paths
