"""
# Maximum Depth in BT
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

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
            return 0
        leftSubTreeDepth = self.maxHeightRecusive(root.left)
        rigtSubTreeDepth = self.maxHeightRecusive(root.right)
        # print([root.data, 1 + max(leftSubTreeDepth, rigtSubTreeDepth), leftSubTreeDepth, rigtSubTreeDepth])
        return 1 + max(leftSubTreeDepth, rigtSubTreeDepth)

    # Time Conmplexity: O(n) | Space Complexity: O(n) (worst case) | O(w) (avg case) where w is the width of the tree
    def maxHeightIterative(self, root):
        if root is None:
            return 0
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
    print("Maxdepth: ", s.maxDepthRecusive(root))
    print("Maxdepth: ", s.maxHeightRecusive(root))
    print("Maxdepth: ", s.maxHeightIterative(root))
