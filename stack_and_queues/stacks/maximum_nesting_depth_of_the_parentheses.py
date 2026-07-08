# Maximum Nesting Depth of the Parentheses


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxLen = 0

        for ch in s:
            if ch == "(":
                stack.append("(")
                maxLen = max(maxLen, len(stack))
            elif ch == ")":
                stack.pop()
        return maxLen
