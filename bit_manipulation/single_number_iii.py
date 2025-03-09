# Single Number III

from typing import List


class Solution1:
    # Function to get the single
    # numbers in the given array
    def singleNumber(self, nums):
        # Variable to store size of array
        n = len(nums)

        # Variable to store XOR of all elements
        XOR = 0

        # Traverse the array
        for i in range(n):
            # Update the XOR
            XOR = XOR ^ nums[i]

        # Variable to get the rightmost
        # set bit in overall XOR
        rightmost = (XOR & (XOR - 1)) ^ XOR

        # Variables to stores XOR of
        # elements in bucket 1 and 2
        XOR1, XOR2 = 0, 0

        # Traverse the array
        for i in range(n):
            # Divide the numbers among bucket 1
            # and 2 based on rightmost set bit
            if nums[i] & rightmost:
                XOR1 = XOR1 ^ nums[i]
            else:
                XOR2 = XOR2 ^ nums[i]

        # Return the result in sorted order
        return [XOR1, XOR2] if XOR1 < XOR2 else [XOR2, XOR1]


class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        return [x, bitmask^x]
