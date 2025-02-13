# LCA in BT

from utils import buildTreeFromArray, TreeNode

from collections import deque


class Solution:
    def distanceK(self, root, target, k):
        pass


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
    print(sol1.distanceK(root))
