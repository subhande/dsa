"""
# Maximum Depth in BT
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

"""
Below is one way to implement a binary tree in Python and write functions to compute the tree’s maximum depth (sometimes also called the height of the tree). Note that depending on your definition, “depth” and “height” can be measured in one of two ways:

1. By counting the number of nodes along the longest path from the root down to a leaf. In this case, an empty tree has a depth (or height) of 0, and a tree with just a root node has a depth of 1.
2. By counting the number of edges along the longest path from the root down to a leaf. In that definition, the root’s depth is 0; an empty tree may be defined to have height –1, and a tree with a single node (root) has height 0.

In the explanation below, we follow the second definition:
 • Depth of the root = 0.
 • The height of any node is the number of edges on the longest downward path from that node.
 • The height (or maximum depth) of the tree is then the height of its root.

"""

class Solution:
    # Time Conmplexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    """
    - Depth of a node is the number of edges from the node to the tree's root node.
    - Root Node Depth = 0
    - Max Depth of a tree is the number of edges on the longest path from the root node to a leaf.
    - Height of a node is the number of edges on the longest path from the node to a leaf.
    - Height of a tree is the height of the root node.
    """
    def maxDepthRecusive(self, root, depth=0):
        if root is None:
            return 0
        leftSubTreeDepth = self.maxDepthRecusive(root.left, depth+1)
        rigtSubTreeDepth = self.maxDepthRecusive(root.right, depth+1)
        # print([root.data, depth, leftSubTreeDepth, rigtSubTreeDepth])
        return max(depth, leftSubTreeDepth, rigtSubTreeDepth)

    # Time Conmplexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def maxHeightRecusive(self, root):
        if root is None:
            return 0 # can also return -1 if height is defined as the number of edges
        leftSubTreeDepth = self.maxHeightRecusive(root.left)
        rigtSubTreeDepth = self.maxHeightRecusive(root.right)
        # print([root.data, 1 + max(leftSubTreeDepth, rigtSubTreeDepth), leftSubTreeDepth, rigtSubTreeDepth])
        return 1 + max(leftSubTreeDepth, rigtSubTreeDepth)

    # Time Conmplexity: O(n) | Space Complexity: O(n) (worst case) | O(w) (avg case) where w is the width of the tree
    def maxHeightIterative(self, root):
        if root is None:
            return 0 # can also return -1 if height is defined as the number of edges
        queue = [root]
        level = 0
        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            level += 1

        return level


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(15)
    root.right.right.right = TreeNode(7)

    s = Solution()
    print("Max Depth: ", s.maxDepthRecusive(root, 0)) # s.maxDepthRecusive(root, 1)) root node can be considered as level 1
    print("Max Height (Recursive): ", s.maxHeightRecusive(root))
    print("Max Height (Iterative): ", s.maxHeightIterative(root))
