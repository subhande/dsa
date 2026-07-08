# Sum of subarray ranges

# Sum of subarray ranges -> Sum of subarray maximums - Sum of subarray minimums

from typing import List


# Approach 1: Brute Force
# Time Complexity: O(n^2) | Space Complexity: O(1)
class Solution1:
    def subArrayRanges(self, nums: List[int]) -> int:
        rangeSum = 0
        n = len(nums)
        for i in range(n):
            largest = smallest = nums[i]
            for j in range(i + 1, n):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])

                rangeSum += largest - smallest
        return rangeSum


# Approach 2: Monotonic Stack
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution2:
    def findNextSmallerElement(self, nums):
        n = len(nums)
        stack = []
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            result[i] = stack[-1] if stack else n
            stack.append(i)
        return result

    def findPrevSmallerElement(self, nums):
        n = len(nums)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            result[i] = stack[-1] if stack else -1
            stack.append(i)
        return result

    def findNextGreaterElement(self, nums):
        n = len(nums)
        stack = []
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            result[i] = stack[-1] if stack else n
            stack.append(i)
        return result

    def findPrevGreaterElement(self, nums):
        n = len(nums)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            result[i] = stack[-1] if stack else -1
            stack.append(i)
        return result

    def subArrayRangesMin(self, nums) -> int:
        n = len(nums)
        left = self.findPrevSmallerElement(nums)
        right = self.findNextSmallerElement(nums)
        result = 0
        for i in range(n):
            result += nums[i] * (i - left[i]) * (right[i] - i)
        return result

    def subArrayRangesMax(self, nums) -> int:
        n = len(nums)
        left = self.findPrevGreaterElement(nums)
        right = self.findNextGreaterElement(nums)
        result = 0
        for i in range(n):
            result += nums[i] * (i - left[i]) * (right[i] - i)
        return result

    def subArrayRanges(self, nums):
        return self.subArrayRangesMax(nums) - self.subArrayRangesMin(nums)
