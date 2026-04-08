# Binary Subarrays With Sum
from typing import List

# Ref: https://youtu.be/j4JDr4-jvo4?si=JbYVXjfcDzQqcy1p


# Sliding Window
class Solution:
    # Helper function to count subarrays with sum at most 'goal'
    def numSubarraysWithSumHelper(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            # No subarray can have a negative sum in a binary array
            return 0
        noOfValidSubArray = 0  # To store the count of valid subarrays
        left = right = 0  # Sliding window pointers
        length = len(nums)
        currSum = 0  # Current sum of the window

        # Expand the window by moving 'right'
        while right < length:
            currSum += nums[right]
            # Shrink the window from the left if the sum exceeds 'goal'
            while currSum > goal:
                currSum -= nums[left]
                left += 1
            # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
            noOfValidSubArray += right - left + 1
            right += 1
        return noOfValidSubArray

    # Main function to count subarrays with sum exactly equal to 'goal'
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # The number of subarrays with sum exactly 'goal' is the difference between:
        # - subarrays with sum at most 'goal'
        # - subarrays with sum at most 'goal - 1'
        return self.numSubarraysWithSumHelper(
            nums, goal
        ) - self.numSubarraysWithSumHelper(nums, goal - 1)


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
