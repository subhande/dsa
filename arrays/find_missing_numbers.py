# Find Missing Number
from typing import List


# Approach 1: Math Formula
# Time Complexity: O(n) | Space Complexity: O(1)
class Solution:
    # Function to find the missing number
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate N from the length of nums
        N = len(nums)

        # Summation of first N natural numbers
        sum1 = (N * (N + 1)) // 2

        # Summation of all elements in nums
        sum2 = sum(nums)

        # Calculate the missing number
        missingNum = sum1 - sum2

        # Return the missing number
        return missingNum

# Approach 2: Bit Manipulation
# Time Complexity: O(n) | Space Complexity: O(1)
# XOR ->
# -> 0 XOR 0 = 0
# -> 0 XOR 1 = 1
# -> 1 XOR 0 = 1
# -> 1 XOR 1 = 0

# Rule: XOR with same number gives 0, and XOR with 0 gives the same number.
#
"""
arr =  [0, 2, 3, 1, 4]

xor1 = 1 ^ 2 ^ 3 ^ 4 ^ 5
xor2 = 0 ^ 2 ^ 3 ^ 1 ^ 4

xor1 ^ xor2 = (1 ^ 2 ^ 3 ^ 4 ^ 5) ^ (0 ^ 2 ^ 3 ^ 1 ^ 4)
            = (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 3) ^ (4 ^ 4) ^ 5 ^ 0
            = 0 ^ 0 ^ 0 ^ 0 ^ 5 ^ 0
            = 5


"""

class Solution2:
    # Function to find the missing number
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0

        # Calculate XOR of all array elements
        for i in range(len(nums)):
            xor1 ^= (i + 1)  # XOR up to [1...N]
            xor2 ^= nums[i]  # XOR of array elements

        # XOR of xor1 and xor2 gives missing number
        return xor1 ^ xor2
