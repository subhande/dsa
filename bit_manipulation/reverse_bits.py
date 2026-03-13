# Reverse Bits

# Approach 1: Bit By Bit Reversal
# Time Complexity: O(1) | Space Complexity: O(1)
# The time complexity is O(1) because we are always processing a fixed number of bits (32 bits for a 32-bit unsigned integer), regardless of the input value.
"""
2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
 1   0   1   0   1   1   0   1
--------------------
 1   0   1   1   0   1   0   1
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            # Get the least significant bit of n and add it to the result at the correct position
            ret += (n & 1) << power
            # Right shift n to process the next bit
            n = n >> 1
            # Decrease the power for the next bit
            power -= 1
        return ret
