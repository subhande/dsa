# Check for symmetrical BTs

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def symmetry(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data != right.data:
            return False
        return self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def is_symmetric(self, root):
        if root is None:
            return True
        return self.symmetry(root.left, root.right)



class Solution2:
    # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
    def is_symmetric_iterative(self, root):
        if root is None:
            return True
        stackLeft, stackRight = [root.left], [root.right]

        while len(stackLeft)  > 0:
            left = stackLeft.pop()
            right = stackRight.pop()

            if left is None and right is None:
                continue

            if left is None or right is None or left.data != right.data:
                return False

            stackLeft.append(left.left)
            stackLeft.append(left.right)
            stackRight.append(right.right)
            stackRight.append(right.left)
        return True


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    s = Solution()
    print(s.is_symmetric(root))

    s2 = Solution2()
    print(s2.is_symmetric_iterative(root))
