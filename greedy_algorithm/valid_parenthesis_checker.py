# Valid Parenthesis Checker

# Dynamic Programming (Recursion + Memoization)
# Time Complexity: O(n^2) | Space Complexity: O(n^2)
class Solution:
    def validString(self, s: str, index: int, open_count: int, dp: list) -> bool:
        if open_count < 0:
            return False
        if index == len(s):
            return open_count == 0
        if dp[index][open_count] != -1:
            return dp[index][open_count]
        res = False
        if s[index] == "(":
            res = self.validString(s, index + 1, open_count + 1, dp)
        elif s[index] == ")":
            res = self.validString(s, index + 1, open_count - 1, dp)
        elif s[index] == "*":
            path_1 = self.validString(s, index + 1, open_count, dp)
            path_2 = self.validString(s, index + 1, open_count + 1, dp)
            path_3 = False
            if open_count > 0:
                path_3 = self.validString(s, index + 1, open_count - 1, dp)
            res = path_1 or path_2 or path_3
        dp[index][open_count] = res
        return res

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.validString(s, 0, 0, dp)


# Greedy Approach

# Time Complexity: O(n) | Space Complexity: O(1)

class Solution2:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen = 0, 0
        for char in s:
            if char == "(":
                minOpen += 1
                maxOpen += 1
            elif char == ")":
                minOpen -= 1
                maxOpen -= 1
            else:
                minOpen -= 1
                maxOpen += 1

            if maxOpen < 0:
                return False

            minOpen = max(0, minOpen)
        return minOpen == 0


# Greedy Approach 2
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution3:
    def checkValidString(self, s: str) -> bool:
        # Stacks to store indices of open brackets and asterisks
        open_brackets = []
        asterisks = []

        for i, ch in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if ch == "(":
                open_brackets.append(i)
            # If current character is an asterisk, push its index onto the stack
            elif ch == "*":
                asterisks.append(i)
            # current character is a closing bracket ')'
            else:
                # If there are open brackets available, use them to balance the closing bracket
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    # If no open brackets are available, use an asterisk to balance the closing bracket
                    asterisks.pop()
                else:
                    # nnmatched ')' and no '*' to balance it.
                    return False

        # Check if there are remaining open brackets and asterisks that can balance them
        while open_brackets and asterisks:
            # If an open bracket appears after an asterisk, it cannot be balanced, return false
            if open_brackets.pop() > asterisks.pop():
                return False  # '*' before '(' which cannot be balanced.

        # If all open brackets are matched and there are no unmatched open brackets left, return true
        return not open_brackets
