# Subtree of Another Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


class Solution2:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        # Check for all subtree rooted at all nodes of tree "root"
        def dfs(node):

            # If this node is Empty, then no tree is rooted at this Node
            # Thus "tree rooted at node" cannot be same as "rooted at subRoot"
            # "tree rooted at subRoot" will always be non-empty (constraints)
            if node is None:
                return False

            # If "tree rooted at node" is identical to "tree at subRoot"
            elif is_identical(node, subRoot):
                return True

            # If "tree rooted at node" was not identical.
            # Check for tree rooted at children
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):

            # If any one Node is Empty, both should be Empty
            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            # Both Nodes Value should be Equal
            # And their respective left and right subtree should be identical
            return (
                node1.val == node2.val
                and is_identical(node1.left, node2.left)
                and is_identical(node1.right, node2.right)
            )

        # Check for node rooted at "root"
        return dfs(root)
