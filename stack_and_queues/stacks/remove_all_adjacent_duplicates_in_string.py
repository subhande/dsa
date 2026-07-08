# Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack or ch != stack[-1]:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)
