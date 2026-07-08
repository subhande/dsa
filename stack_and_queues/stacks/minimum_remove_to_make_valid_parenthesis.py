# Minimum Remove to Make Valid Parentheses


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexes_to_remove = set()

        count = 0

        for idx, ch in enumerate(s):
            if ch not in "()":
                continue
            elif ch == "(":
                stack.append(idx)
            elif not stack:
                indexes_to_remove.add(idx)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))

        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)


class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        present = [True] * len(s)

        count = 0

        for idx, ch in enumerate(s):
            if ch == ")" and not stack:
                count += 1
                present[idx] = False
            elif ch == "(":
                stack.append(("(", idx))
            elif ch == ")":
                stack.pop()
        while stack:
            ele = stack.pop()
            present[ele[1]] = False

        validString = ""
        for idx in range(len(s)):
            if present[idx]:
                validString += s[idx]

        return validString
