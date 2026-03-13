# Single Number II
# https://leetcode.com/problems/single-number-ii/description/
from typing import List

"""
[5, 5, 5, 6, 4, 4, 4]

            1 0 1
            1 0 1
            1 0 1
            1 1 0
            1 0 0
            1 0 0
            1 0 0
            ------
bit sum ->  7 1 3
bit sum % 3 -> 1 1 0 -> loner = 6
Assuming 32 bit integers, we can iterate over all bits and compute the sum of bits at that position for all integers in the array.
Positions are 0 to 31, and for each position, we can compute the bit of the loner at that position by taking the sum of bits at that position modulo 3.

e.g. If postion 0 has a bit sum of 7, then the bit of the loner at position 0 is 7 % 3 = 1.


"""
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

"""

A number can be added to Ones if it is not already in Twos.
A number can be added to Twos if it is already in Ones.
A number can be added to Threes if it is already in Twos.

Ones = (Ones ^ num) & ~Twos;
Twos = (Twos ^ num) & ~Ones;

When a number appears for the first time, it will be added to Ones.
When the same number appears for the second time, it will be moved from Ones to Twos.
When the same number appears for the third time, it will be removed from both Ones and Twos.
"""
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
