# Maximum Subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingHere = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            maxEndingHere = max(num, maxEndingHere + num)
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
