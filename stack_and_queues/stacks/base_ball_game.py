from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []

        for operation in operations:
            if operation == "C":
                scores.pop()
            elif operation == "D":
                scores.append(scores[-1] * 2)
            elif operation == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(operation))
        return sum(scores)
