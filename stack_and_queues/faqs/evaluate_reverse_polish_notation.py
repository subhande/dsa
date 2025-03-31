
# Evaluate Reverse Polish Notation
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_map = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: (x/y)
        }
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                if len(stack) >= 2:
                    second = int(stack.pop())
                    first = int(stack.pop())
                    # print([first, second, token, op_map[token](first, second)])
                    stack.append(op_map[token](first, second))
        return int(stack[-1])
