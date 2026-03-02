# First Missing Positive

from typing import List


# Here maximum value of missing positive number can be n+1, where n is the length of the array.
# For example, if the array contains all numbers from 1 to n, then the missing positive number would be n+1.
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxPossibleValue = len(nums) + 1
        numsMap = {}
        for num in nums:
            if num >= 0:
                numsMap[num] = True
        for i in range(1, maxPossibleValue+1):
            if i not in numsMap:
                return i
        return -1


# Time Complexity: O(n) | Space Complexity: O(1)
# Pass 1: Mark all negative numbers as 0
# Pass 2: Mark the presence of numbers in the array by negating the value at the corresponding index
# Pass 3: Find the first index with a positive value, which indicates the missing positive number
"""
nums = [3, -3, 6, 3, 2]
Pass 1: nums = [3, 0, 6, 3, 2]
Pass 2: nums = [-3, -6, -6, 3, 2]
Pass 3: The first index with a positive value is at index 0, which indicates
the missing positive number is 1.
"""
class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Pass 1: Mark all negative numbers as 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # Pass 2: Mark the presence of numbers in the array
        for i in range(n):
            num = abs(nums[i])
            if num > 0 and num <= n:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
                elif nums[num - 1] == 0:
                    nums[num - 1] = -(n + 1)

        # Pass 3: Find the first index with a positive value
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1
