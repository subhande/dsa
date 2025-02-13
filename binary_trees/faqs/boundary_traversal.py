# Boundary Traversal


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right




class Solution:
    def isLeaf(self, node):
        return node.left is None and node.right is None
    def leftBoundary(self, node, boundary):
        if node is None:
            return
        if self.isLeaf(node):
            return
        boundary.append(node.data)
        if node.left is not None:
            self.leftBoundary(node.left, boundary)
        elif node.right is not None:
            self.leftBoundary(node.right, boundary)
        return
    def rightBoundary(self, node, boundary):
        if node is None:
            return
        if self.isLeaf(node):
            return

        if node.right is not None:
            self.rightBoundary(node.right, boundary)
        elif node.left is not None:
            self.rightBoundary(node.left, boundary)
        boundary.append(node.data)
        return

    def leafNodes(self, node, boundary):
        if node is None:
            return
        if self.isLeaf(node):
            boundary.append(node.data)
            return
        self.leafNodes(node.left, boundary)
        self.leafNodes(node.right, boundary)

    # Time Complexity: O(n) | Space Complexity: O(n) (worst case for skewed tree)
    def boundary(self, root):
        boundary = []
        if root is None:
            return
        if not self.isLeaf(root):
            boundary.append(root.data)
        self.leftBoundary(root.left, boundary)
        self.leafNodes(root, boundary)
        self.rightBoundary(root.right, boundary)
        return boundary

class Solution2:
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def leftBoundary(self, node, boundary):
        while node:
            if not self.isLeaf(node):
                boundary.append(node.data)
            if node.left:
                node = node.left
            else:
                node = node.right
    def rightBoundary(self, node, boundary):
        temp = []
        while node:
            if not self.isLeaf(node):
                temp.append(node.data)
            if node.right:
                node = node.right
            else:
                node = node.left
        boundary.extend(temp[::-1])

    def leafNodes(self, node, boundary):
        if node is None:
            return
        if self.isLeaf(node):
            boundary.append(node.data)
            return
        self.leafNodes(node.left, boundary)
        self.leafNodes(node.right, boundary)

    # Time Complexity: O(n) | Space Complexity: O(n) (worst case for skewed tree)
    def boundary(self, root):
        boundary = []
        if root is None:
            return
        if not self.isLeaf(root):
            boundary.append(root.data)
        self.leftBoundary(root.left, boundary)
        self.leafNodes(root, boundary)
        self.rightBoundary(root.right, boundary)
        return boundary

def buildTreeFromArray(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = q[front]
        front += 1

        item = arr[index]
        index += 1
        if item is not None:
            node.left = TreeNode(item)
            q.append(node.left)

        if index >= len(arr):
            break

        item = arr[index]
        index += 1
        if item is not None:
            node.right = TreeNode(item)
            q.append(node.right)
    return root

if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.left.right.left = TreeNode(8)
    # root.left.right.right = TreeNode(9)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    s = Solution2()
    print(s.boundary(root))

    tree = [1 ,None, 15, 69 ,None ,None, 97 ,None, 96, 45 ,None, None, 70 ,None, 61 ,None, 67 ,None, 55 ,None ,None]
    root = buildTreeFromArray(tree)
    print(s.boundary(root))
    # print_tree(tree)
