# Koko eating bananas

import math
class Solution:
    def calculateTotalHours(self, nums, hourly):
        totalH = 0
        n = len(nums)

        # Calculate total hours required
        for i in range(n):
            totalH += math.ceil(nums[i] / hourly)
        return totalH
    def minimumRateToEatBananas(self, nums, h):
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            totalH = self.calculateTotalHours(nums, mid)

            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
