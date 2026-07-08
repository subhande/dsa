# Valid Parenthesis


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif bracket == ")" and len(stack) and stack[-1] == "(":
                stack.pop()
            elif bracket == "]" and len(stack) and stack[-1] == "[":
                stack.pop()
            elif bracket == "}" and len(stack) and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if len(stack) == 0 or ch in ["(", "[", "{"]:
                stack.append(ch)
            elif stack[-1] == "(" and ch == ")":
                stack.pop()
            elif stack[-1] == "[" and ch == "]":
                stack.pop()
            elif stack[-1] == "{" and ch == "}":
                stack.pop()
            else:
                break

        return True if len(stack) == 0 else False
