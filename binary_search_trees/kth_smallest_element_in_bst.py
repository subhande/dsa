

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        def inorder(node: TreeNode | None):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)[k-1]