from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        left, right = 0, 0
        n = len(nums)

        product = 1

        noOfSubarrays = 0

        while right < n:
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            noOfSubarrays += right - left + 1

            right += 1

        return noOfSubarrays
