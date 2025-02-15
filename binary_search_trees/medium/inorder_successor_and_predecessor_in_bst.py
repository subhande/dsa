import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray



class Solution1:
    def inorderTraversal(self, root, inorder):
        if root:
            self.inorderTraversal(root.left, inorder)
            inorder.append(root.data)
            self.inorderTraversal(root.right, inorder)

    # Time Complexity: O(n) | Space Complexity: O(n)
    def succPredBSTUsingInOder(self, root, key):
        # Find the inorder traversal of the BST
        inorder = []
        self.inorderTraversal(root, inorder)
        # Find the index of the key in the inorder traversal
        index = inorder.index(key)
        # Find the predecessor and successor of the key
        pred = inorder[index-1] if index > 0 else -1
        succ = inorder[index+1] if index < len(inorder)-1 else -1
        return [pred, succ]

    # Time Complexity: O(h) | Space Complexity: O(1)
    def succPredBSTOptimized(self, root, key):
            # Initialize successor and predecessor as None.
            successor, predecessor = None, None
            # Start the traversal from the root node.
            current = root

            # Iterate until there is no node to process.
            while current:
                # If the current node's data matches the key,
                # then look for the successor and predecessor within its subtrees.
                if current.data == key:
                    # Finding the inorder successor in the right subtree.
                    if current.right:
                        successor = current.right
                        # The leftmost node in the right subtree is the inorder successor.
                        while successor.left:
                            successor = successor.left
                    # Finding the inorder predecessor in the left subtree.
                    if current.left:
                        predecessor = current.left
                        # The rightmost node in the left subtree is the inorder predecessor.
                        while predecessor.right:
                            predecessor = predecessor.right
                    # Once both are found (if they exist), break out of the loop.
                    break

                # If key is greater than current node's data,
                # then current node could be a predecessor.
                elif current.data < key:
                    # Assign current node as the latest potential predecessor.
                    predecessor = current
                    # Move to the right subtree since all keys to the right are larger.
                    current = current.right

                # If key is less than current node's data,
                # then current node could be a successor.
                elif key < current.data:
                    # Assign current node as the latest potential successor.
                    successor = current
                    # Move to the left subtree since all keys to the left are smaller.
                    current = current.left

            # Return the data for predecessor and successor.
            # If a predecessor or successor doesn't exist, return -1.
            return [predecessor.data if predecessor else -1, successor.data if successor else -1]

if __name__ == "__main__":
    sol1 = Solution1()

    # Test 1
    root = [5, 2, 10, 1, 4, 7, 12]
    key = 10
    root = buildTreeFromArray(root)
    print(sol1.succPredBSTUsingInOder(root, key)) # [7, 12]
    print(sol1.succPredBSTOptimized(root, key)) # [7, 12]

    # Test 2
    root =  [5, 2, 10, 1, 4, 7, 12]
    key = 12
    root = buildTreeFromArray(root)
    print(sol1.succPredBSTUsingInOder(root, key)) # [10, -1]
    print(sol1.succPredBSTOptimized(root, key)) # [10, -1]
