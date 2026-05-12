# Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            miHeight = min(height[left], height[right])
            maxarea = max(maxarea, miHeight * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea


class Solution3:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        maxStoredWater = 0

        while left < right:
            maxStoredWater = max(
                maxStoredWater, min(height[left], height[right]) * (right - left)
            )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxStoredWater
