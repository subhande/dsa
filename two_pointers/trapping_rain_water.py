# Trapping Rain Water

from typing import List


# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max_h = 0
        right_max_h = 0

        for i in range(n):
            left_max_h = max(height[i], left_max_h)
            left_max[i] = left_max_h
        for i in range(n-1, -1, -1):
            right_max_h = max(height[i], right_max_h)
            right_max[i] = right_max_h
        total = 0

        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]
        return total

# Time Complexity: O(n) | Space Complexity: O(1)
class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
