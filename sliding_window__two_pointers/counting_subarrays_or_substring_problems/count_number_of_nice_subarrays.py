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


class Solution2:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            # Find subarrays with sum k ending at i
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            # Increment the current prefix sum in hashmap
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return subarrays
