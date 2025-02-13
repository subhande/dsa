
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        elif self.left is None:
            return f"""{str(self.data)} {str(self.right)}"""
        elif self.right is None:
            return f"""{str(self.data)} {str(self.left)}"""
        else:
            return f"""{str(self.data)} {str(self.left)} {str(self.right)}"""
    def __eq__(self, other):
        return self.data == other.data and self.left == other.left and self.right == other.right

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
