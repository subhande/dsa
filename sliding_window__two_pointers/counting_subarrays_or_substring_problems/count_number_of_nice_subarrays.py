# Count number of Nice subarrays
from typing import List
class Solution:
    def numberOfSubarraysHelper(self, nums: List[int], k: int) -> int:
        left = right = 0
        validSubArrayCount = 0
        length = len(nums)
        currSubArrayOddNumberCount = 0
        while right < length:
            if nums[right] % 2 == 1:
                currSubArrayOddNumberCount += 1
            while currSubArrayOddNumberCount > k:
                if nums[left] % 2 == 1:
                    currSubArrayOddNumberCount -= 1
                left += 1
            validSubArrayCount += right - left + 1
            right += 1
        return validSubArrayCount



    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numberOfSubarraysHelper(nums, k) - self.numberOfSubarraysHelper(nums, k-1)
