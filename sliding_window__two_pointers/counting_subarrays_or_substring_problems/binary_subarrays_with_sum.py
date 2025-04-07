# Binary Subarrays With Sum

# Sliding Window
from typing import List
class Solution:
    def numSubarraysWithSumHelper(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
        noOfValidSubArray = 0
        left = right = 0
        length = len(nums)
        currSum = 0
        while right < length:
            currSum += nums[right]
            while currSum > goal:
                currSum -= nums[left]
                left += 1
            noOfValidSubArray += (right - left + 1)
            right += 1
        return noOfValidSubArray
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.numSubarraysWithSumHelper(nums, goal) - self.numSubarraysWithSumHelper(nums, goal-1)

# Prefix Sum

class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {}  # To store the frequency of prefix sums

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1

            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count
# Solution2 and Solution3 are the same but freq is initialized differently
class Solution3:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {0: 1}  # To store the frequency of prefix sums

        for num in nums:
            current_sum += num

            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count
