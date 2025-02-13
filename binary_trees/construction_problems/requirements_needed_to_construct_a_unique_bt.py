# Requirements needed to construct a unique BT

"""
Pre-Order: Root, Left, Right -> 1
In-Order: Left, Root, Right -> 2
Post-Order: Left, Right, Root -> 3

"""

class Solution:
    def unique_binary_tree(self, a, b):
        return not (a == b or (a == 1 and b == 3) or (a == 3 and b == 1))

if __name__ == "__main__":
    solution = Solution()
    # Example test cases
    print(solution.unique_binary_tree(1, 2))
    print(solution.unique_binary_tree(1, 3))
