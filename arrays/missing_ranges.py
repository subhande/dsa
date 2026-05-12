from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:

        missing_ranges = []

        if len(nums) == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges

        # Check for any missing numbers between the lower bound and nums[0].
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # Check for any missing numbers between successive elements of nums.
        for i in range(1, len(nums)):
            prevEle = nums[i - 1]
            currEle = nums[i]

            if currEle - prevEle <= 1:
                continue

            missing_ranges.append([prevEle + 1, currEle - 1])

        # Check for any missing numbers between the last element of nums and the upper bound.
        if nums[-1] < upper:
            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges
