# Single Number II
# https://leetcode.com/problems/single-number-ii/description/
from typing import List

# Time Complexity: 32 * O(n) = O(n). | Space Complexity: O(1).
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:

        # Loner.
        loner = 0

        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0

            # For this bit, iterate over all integers
            for num in nums:

                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1

            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        # Do not mistaken sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner


# Time Complexity: O(n) | Space Complexity: O(1).
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:

        # Initialize seen_once and seen_twice to 0
        seen_once = seen_twice = 0

        # Iterate through nums
        for num in nums:
            # Update using derived equations
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)

        # Return integer which appears exactly once
        return seen_once
