# Minimize XOR
# https://leetcode.com/problems/minimize-xor/?envType=problem-list-v2&envId=bit-manipulation

# Time complexity: O(logn) | Space complexity: O(1)
"""
Let n be the maximum possible value of num1 or num2.

Time Complexity: O(logn).

The time complexity of the given solution is O(logn). This is because the algorithm primarily involves two operations: counting the number of set bits in the integers and adjusting the set bits of result to match the target count. The counting of set bits requires iterating over the binary representation of the integer, which takes O(logn) time since the number of bits in an integer is proportional to logn.

Additionally, the while loops iterate over the bits of result, setting or unsetting bits as needed, which also takes logn time in the worst case, as we may need to process up to all 32 bits. The helper functions (isSet, setBit, and unsetBit) involve constant-time bitwise operations and do not impact the overall complexity.

As a result, the time complexity is dominated by the bit manipulation and bit counting operations, both of which are O(logn).

Space Complexity: O(1).

We only use a fixed number of variables and therefore the algorithm requires constant extra space.

"""
class Solution1:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Initialize result to num1. We will modify result.
        result = num1

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = bin(result).count("1")

        # Start with the least significant bit (bit 0).
        current_bit = 0

        # Add bits to result if it has fewer set bits than the target.
        while set_bits_count < target_set_bits_count:
            # If the current bit in result is not set (0), set it to 1.
            if not self._is_set(result, current_bit):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            # Move to the next bit.
            current_bit += 1

        # Remove bits from result if it has more set bits than the target.
        while set_bits_count > target_set_bits_count:
            # If the current bit in result is set (1), unset it (make it 0).
            if self._is_set(result, current_bit):
                result = self._unset_bit(result, current_bit)
                set_bits_count -= 1
            # Move to the next bit.
            current_bit += 1

        return result

    # Helper function to check if the given bit position in result is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in result to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

    # Helper function to unset the given bit position in x (set it to 0).
    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)

class Solution2:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  # Start from the most significant bit.

        # While result has fewer set bits than num2
        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1  # Move to the next bit.
        return result

    # Helper function to check if the given bit position in x is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in x to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)


if __name__ == "__main__":
    solution1 = Solution1()
    solution2 = Solution2()

    # Example 1
    num1 = 3
    num2 = 5
    assert solution1.minimizeXor(num1, num2) == 3
    assert solution2.minimizeXor(num1, num2) == 3

    # Example 2
    num1 = 1
    num2 = 12
    assert solution1.minimizeXor(num1, num2) == 3
    assert solution2.minimizeXor(num1, num2) == 3

    print("All tests passed.")
