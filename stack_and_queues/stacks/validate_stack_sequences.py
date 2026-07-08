# Validate Stack Sequences

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        i, j = 0, 0
        n = len(pushed)
        while i < n:
            if not stack:
                stack.append(pushed[i])
                i += 1
            else:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
        while stack and j < n and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        return True if not stack else False


class Solution2(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
