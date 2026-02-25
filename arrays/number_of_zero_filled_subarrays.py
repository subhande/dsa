# Number Of Zero-Filled Subarrays

from typing import List


class Solution:
    # Time Complexity: O(n) | Space Complexity: O(n)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lengthsOfZeroSubArrays = []
        currZeroSubArrLength = 0
        for num in nums:
            if num == 0:
                currZeroSubArrLength += 1
            else:
                if currZeroSubArrLength > 0:
                    lengthsOfZeroSubArrays.append(currZeroSubArrLength)
                    currZeroSubArrLength = 0
        if currZeroSubArrLength > 0:
            lengthsOfZeroSubArrays.append(currZeroSubArrLength)

        totalNumberOfZeroSubarrays = sum([(length * (length +1 ))//2 for length in lengthsOfZeroSubArrays])

        return totalNumberOfZeroSubarrays

    # Time Complexity: O(n) | Space Complexity: O(1)
    def zeroFilledSubarray2(self, nums: List[int]) -> int:
        currZeroSubArrLength = 0
        totalNumberOfZeroSubarrays = 0
        for num in nums:
            if num == 0:
                currZeroSubArrLength += 1
            else:
                if currZeroSubArrLength > 0:
                    totalNumberOfZeroSubarrays += (currZeroSubArrLength * (currZeroSubArrLength + 1 ))//2
                    currZeroSubArrLength = 0
        if currZeroSubArrLength > 0:
            totalNumberOfZeroSubarrays += (currZeroSubArrLength * (currZeroSubArrLength + 1 ))//2
        return totalNumberOfZeroSubarrays

    # Time Complexity: O(n) | Space Complexity: O(1)
    """
    Explanation with example:
    arr = [0, 0, 0, 1, 0]
    currZeroSubArrLength = 0, totalNumberOfZeroSubarrays = 0
    num = 0 -> currZeroSubArrLength = 1, totalNumberOfZeroSubarrays = 1
    num = 0 -> currZeroSubArrLength = 2, totalNumberOfZeroSubarrays = 1 + 2 = 3
    num = 0 -> currZeroSubArrLength = 3, totalNumberOfZeroSubarrays = 3 + 3 = 6
    num = 1 -> currZeroSubArrLength = 0, totalNumberOfZeroSubarrays = 6
    num = 0 -> currZeroSubArrLength = 1, totalNumberOfZeroSubarrays = 6 + 1 = 7

    """
    def zeroFilledSubarray3(self, nums: List[int]) -> int:
            currZeroSubArrLength = 0
            totalNumberOfZeroSubarrays = 0
            for num in nums:
                if num == 0:
                    currZeroSubArrLength += 1
                else:
                    currZeroSubArrLength = 0
                totalNumberOfZeroSubarrays += currZeroSubArrLength
            return totalNumberOfZeroSubarrays
