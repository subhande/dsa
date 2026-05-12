# Approach 1: Brute Force
# Time Complexity: O(n^2) | Space Complexity: O(n)


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False


# Approach 2: Concatenation Check
# Time Complexity: O(n^2) | Space Complexity: O(1)
class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


# Approach 3: KMP Algorithm
# TODO: Implement KMP Algorithm for string matching
