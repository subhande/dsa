# 132 Pattern

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        currMin = nums[0]
        for index in range(1, n):
            while stack and stack[-1][0] <= nums[index]:
                stack.pop()
            if stack and nums[index] > stack[-1][1]:
                return True
            stack.append((nums[index], currMin))
            currMin = min(currMin, nums[index])
        return False
