import os, sys
# Determine the project root relative to this file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from binary_search_trees.utils import TreeNode, buildTreeFromArray


# Floor and Ceil in a BST

class Solution:
    # Time Compexity: O(h) | Space Complexity: O(1)
    def floorCeilOfBST(self, root, key):
        floor, ceil = -1, -1

        # Find floor
        current = root
        while current:
            if current.data == key:
                floor = current.data
                break
            elif current.data < key:
                floor = current.data
                current = current.right
            else:
                current = current.left

        # Find ceil
        current = root
        while current:
            if current.data == key:
                ceil = current.data
                break
            elif current.data > key:
                ceil = current.data
                current = current.left
            else:
                current = current.right

        return [floor, ceil]

    # Time Compexity: O(h) | Space Complexity: O(1)
    def floorCeilOfBSTOptimized(self, root, key):
            floor, ceil = -1, -1

            # Find floor and ceil
            current = root
            while current:
                if current.data == key:
                    floor = current.data
                    ceil = current.data
                    break
                elif current.data < key:
                    floor = current.data
                    current = current.right
                elif current.data > key:
                    ceil = current.data
                    current = current.left

            return [floor, ceil]





if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root =  [8, 4, 12, 2, 6, 10, 14]
    key = 11
    root = buildTreeFromArray(root)
    print(sol.floorCeilOfBST(root, key))
    print(sol.floorCeilOfBSTOptimized(root, key))


    # Test 2
    root = [8, 4, 12, 2, 6, 10, 14]
    key = 15
    root = buildTreeFromArray(root)
    print(sol.floorCeilOfBST(root, key))
    print(sol.floorCeilOfBSTOptimized(root, key))
