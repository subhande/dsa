# Basic Calculator II


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        s = "".join(s.split(" "))
        num = 0
        n = len(s)
        operation = "+"
        for index in range(n):
            ch = s[index]
            if ch == " ":
                continue
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in ops or index == n-1:
                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif operation == '/':
                    prev = stack.pop()
                    # Python division truncates towards negative infinity so we adjust to truncate toward zero.
                    if prev < 0:
                        stack.append(- (abs(prev) // num))
                    else:
                        stack.append(prev // num)
                operation = ch
                num = 0  # reset number for next round
        # The final answer is the sum of the numbers in the stack.
        return sum(stack)
