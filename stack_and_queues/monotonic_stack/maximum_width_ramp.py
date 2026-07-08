# Maximum Width Ramp

from typing import List


# Approach: Two Pointers with Preprocessing
class Solution1:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [-1] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        right = 0
        max_width = 0
        # print(right_max)
        # Traverse the array using left and right pointers
        while right < n:
            # print([nums[left], right_max[right]], nums[left] > right_max[right])
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width


# Approach: Monotonic Stack
class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        indices_stack = []

        # Fill the stack with indices in increasing order of their values
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)

        max_width = 0

        # Traverse the array from the end to the start
        for j in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                # Pop the index since it's already processed
                indices_stack.pop()

        return max_width
