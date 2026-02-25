# Move zeros to end
from typing import List


# Brute Force Solution:
# Time Complexity: O(n) | Space Complexity: O(n)
# Pseudo Code:
# 1. Create a new array of the same size as the input array, initialized with
# 2. Iterate through the input array and copy all non-zero elements to the new array.
# 3. Copy the elements from the new array back to the original array.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        arr_idx = 0
        for i in range(n):
            if nums[i] != 0:
                arr[arr_idx] = nums[i]
                arr_idx += 1
        for i in range(n):
            nums[i] = arr[i]

# Optimal Solution:
# Time Complexity: O(n) | Space Complexity: O(1)
# Pseudo Code:
# 1. Initialize a variable lastNonZeroFoundAt to keep track of the position of the last non-zero element found.
# 2. Iterate through the input array:
#    a. If the current element is non-zero, copy it to the position indicated by lastNonZeroFoundAt and increment lastNonZeroFoundAt.
# 3. After the loop, all non-zero elements are in their correct positions, and lastNonZeroFoundAt indicates the index where the first zero should be placed.
"""
arr = [0, 1, 4, 0, 5, 2]
lastNonZeroFoundAt = 0, i = 0
nums = [0, 1, 4, 0, 5, 2]
lastNonZeroFoundAt = 0, i = 1
nums = [1, 1, 4, 0, 5, 2]
lastNonZeroFoundAt = 1, i = 2
nums = [1, 4, 4, 0, 5, 2]
lastNonZeroFoundAt = 2, i = 3
nums = [1, 4, 4, 0, 5, 2]
lastNonZeroFoundAt = 2, i = 4
nums = [1, 4, 5, 0, 5, 2]
lastNonZeroFoundAt = 3, i = 5
nums = [1, 4, 5, 2, 5, 2]

nums = [1, 4, 5, 2, 0, 0]

"""
class SolutionOptimal:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
