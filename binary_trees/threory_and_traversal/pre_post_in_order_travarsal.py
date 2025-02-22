"""
# Pre, Post, Inorder in one traversal
"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def tree_traversal(self, root: TreeNode | None):
        pre_order, post_order, in_order = [], [], []
        stack = []
        stack.append((root, 1))
        while stack:
            node, state = stack.pop()
            if node is None:
                continue
            if state == 1:
                pre_order.append(node.value)
                stack.append((node, 2))
                stack.append((node.left, 1))
            elif state == 2:
                in_order.append(node.value)
                stack.append((node, 3))
                stack.append((node.right, 1))
            else:
                post_order.append(node.value)
        return pre_order, in_order, post_order



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    s = Solution()
    for i, traversal in enumerate(s.tree_traversal(root)):
        if i == 0:
            print("===== Pre Order Traversal =====")
            print(traversal)
        elif i == 1:
            print("===== In Order Traversal =====")
            print(traversal)
        else:
            print("===== Post Order Traversal =====")
            print(traversal)
    # print(s.preOrderIterative(root))
