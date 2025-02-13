# LCA in BT

from utils import buildTreeFromArray, TreeNode

from collections import deque



class Solution:
    def getPathFromRoot(self, root, node, path:list):
        if not root:
            return False
        path.append(root)
        if root == node:
            return True
        if self.getPathFromRoot(root.left, node, path) or self.getPathFromRoot(root.right, node, path):
            return True
        path.pop()
        return False

    # Time Complexity: O(n) | Space Complexity: O(n)
    def lowestCommonAncestorBruteForce(self, root, p, q):
        p_path, q_path = [], []
        self.getPathFromRoot(root, p, p_path)
        self.getPathFromRoot(root, q, q_path)
        # print([node.data for node in p_path])
        # print([node.data for node in q_path])
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i].data != q_path[i].data:
                break
            i += 1
        return p_path[i-1]

    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def lowestCommonAncestorOptimized(self, root, p, q):
        # base Case
        if root is None or root == p or root == q:
            return root

        # Search left and right subtree
        left = self.lowestCommonAncestorOptimized(root.left, p, q)
        right = self.lowestCommonAncestorOptimized(root.right, p, q)

        # If both left and right are not None, then root is the LCA
        # If one of the left or right is None, then the other is the LCA
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    root = buildTreeFromArray(  [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = root.left, root.right
    # LCA: 3
    print(sol.lowestCommonAncestorBruteForce(root, p, q))
    print(sol.lowestCommonAncestorOptimized(root, p, q))



    # Test Case 2
    root = buildTreeFromArray([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = root.left, root.left.right.right
    print(sol.lowestCommonAncestorBruteForce(root, p, q))
    print(sol.lowestCommonAncestorOptimized(root, p, q))
