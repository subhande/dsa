# Daily Temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        temperatures_delta = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                temperatures_delta[i] = stack[-1] - i
            stack.append(i)

        return temperatures_delta


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        temperatures_delta = [0] * n

        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                i = stack.pop()
                temperatures_delta[i] = idx - i

            stack.append(idx)
        return temperatures_delta
