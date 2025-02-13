# Serialize and De-serialize BT
from utils import buildTreeFromArray, TreeNode
from collections import deque

class Solution:
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: string
        """

        if not root:
            return ""

        # Initialize an empty string to store the serialized data
        result = []
        # Use a queue for level-order traversal
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                # Push the left and right children to the queue for further traversal
                queue.append(node.left)
                queue.append(node.right)

        # Return the serialized string
        return ",".join(result)

    def deserialize(self, data):
        """
        :type root: string
        :rtype: TreeNode
        """

        if not data:
            return None

        # Use a deque to tokenize the serialized data
        tokens = deque(data.split(","))

        # Read the root value from the serialized data
        root = TreeNode(int(tokens.popleft()))

        # Use a queue for level-order traversal
        queue = deque([root])

        # Perform level-order traversal to reconstruct the tree
        while queue:
            node = queue.popleft()

            # Read the left child value from the serialized data
            left = tokens.popleft()
            if left != "#":
                node.left = TreeNode(int(left))
                queue.append(node.left)

            # Read the right child value from the serialized data
            right = tokens.popleft()
            if right != "#":
                node.right = TreeNode(int(right))
                queue.append(node.right)

        # Return the root of the reconstructed tree
        return root


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = buildTreeFromArray([2, 1, 3])
    print(tree)
    serialized = sol.serialize(tree)
    print(serialized)
    result = sol.deserialize(serialized)
    print(result)

    # Test 2
    tree = buildTreeFromArray([10, 20, 30, 40, 50, 60])
    print(tree)
    serialized = sol.serialize(tree)
    print(serialized)
    result = sol.deserialize(serialized)
    print(result)
