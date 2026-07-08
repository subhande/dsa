# Buildings with an ocean view

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        oceanView = [-1] * n

        for idx in range(n):
            while stack and heights[stack[-1]] <= heights[idx]:
                oceanView[stack.pop()] = heights[idx]

            stack.append(idx)
            print(stack, oceanView)

        return [i for i in range(n) if oceanView[i] == -1]


class Solution2:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []

        for idx in range(n):
            while stack and heights[stack[-1]] <= heights[idx]:
                stack.pop()

            stack.append(idx)
        return stack
