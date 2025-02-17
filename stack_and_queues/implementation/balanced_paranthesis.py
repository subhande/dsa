# Blanced Paranthesis


class Solution:
    def isValid(self, str: str) -> bool:
        stack = []
        for i in str:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()

    # Test 1
    s = "()"
    # Output: True
    print(sol.isValid(s))

    # Test 2
    s = "()[(]{}"
    # Output: True
    print(sol.isValid(s))

    # Test 3
    s = "[()]"
    # Output: False
    print(sol.isValid(s))
