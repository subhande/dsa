# 132 Pattern
# https://www.youtube.com/watch?v=q5ANAl8Z458
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Stack to store pairs of (current number, minimum value seen so far)
        stack = []
        n = len(nums)
        # Track the minimum value seen so far
        currMin = nums[0]

        # Iterate through the array starting from index 1
        for index in range(1, n):
            # Pop elements from stack while current number is greater than or equal to stack top
            while stack and stack[-1][0] <= nums[index]:
                stack.pop()

            # Check if we found a 132 pattern: currMin < current number && current number < stack top
            # curr Min Index < stack top Index < current number Index
            # Curr Min < Current Number < Stack Top
            if stack and nums[index] > stack[-1][1]:
                return True

            # Push current number with its corresponding minimum
            stack.append((nums[index], currMin))
            # Update the minimum value seen so far
            currMin = min(currMin, nums[index])

        return False
