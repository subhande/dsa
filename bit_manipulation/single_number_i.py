# Single Number I
# https://leetcode.com/problems/single-number/
from typing import List
# Time complexity: O(n) | Space complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result

class SolutionExtended1:
    def find_unique(self, nums, duplicate_count=2, unique_count=1):
        """
        Finds the unique number in a list where every other number appears exactly
        duplicate_count times and one unique number appears unique_count times.

        Parameters:
          nums           : List[int] - the list of integers.
          duplicate_count: int - how many times every non-unique number appears.
          unique_count   : int - how many times the unique number appears.
          Constraints:
              unique_count < duplicate_count

        Returns:
          int : The unique number.

        Note:
          This approach works if unique_count modulo duplicate_count is not 0.
        """
        result = 0
        # We assume 32-bit integers. If the numbers can be larger, adjust the range.
        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Extract the i-th bit and add it to the sum.
                bit_sum += (num >> i) & 1

            # All duplicate numbers contribute a multiple of duplicate_count.
            # So if the unique number has a 1 in this bit, then bit_sum will be:
            #   duplicate_contrib + unique_count
            # Therefore, if bit_sum % duplicate_count equals unique_count % duplicate_count,
            # we assume that bit is 1 in the unique number.
            if bit_sum % duplicate_count == unique_count % duplicate_count:
                result |= (1 << i)

        # To handle negative numbers (if using 32-bit signed integers)
        if result >= 2**31:
            result -= 2**32

        # Now verify that candidate appears exactly unique_count times.
        if nums.count(result) != unique_count:
            return "Not found"

        return result

# Example usage:
# Does not work if unique_count >= duplicate_count
if __name__ == "__main__":
    sol_ext1 = SolutionExtended1()
    # Standard case: duplicates appear twice and unique appears once.
    nums1 = [2, 3, 2, 4, 4]
    print("Unique (duplicates twice, unique once):", sol_ext1.find_unique(nums1, duplicate_count=2, unique_count=1))

    nums1 = [2, 3, 2, 3, 4, 3, 4, 4]
    print("Unique (duplicates thrice, unique twice):", sol_ext1.find_unique(nums1, duplicate_count=3, unique_count=2))


    nums2 = [7, 5, 5, 5, 9, 9, 9]
    print("Unique (duplicates twice, unique 4 times):", sol_ext1.find_unique(nums2, duplicate_count=3, unique_count=4))

    nums2 = [7, 7, 7, 7, 5, 5, 5, 9, 9, 9]
    print("Unique (duplicates twice, unique 4 times):", sol_ext1.find_unique(nums2, duplicate_count=3, unique_count=4))
