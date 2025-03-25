# Max Consecutive Ones III
from typing import List

class Solution:
    # Time Complexity: O(2n) | Space Complexity: O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        currSum = 0
        maxLen = 0
        while right < n:
            currSum += nums[right]
            length = right - left + 1
            while length > currSum + k:
                currSum -= nums[left]
                left += 1
                length = right - left + 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen

    # Efficitly moving the left pointer to the right by 1
    # Time Complexity: O(n) | Space Complexity: O(1)
    def longestOnes2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        currSum = 0
        maxLen = 0
        while right < n:
            currSum += nums[right]
            length = right - left + 1
            if length > currSum + k:
                currSum -= nums[left]
                left += 1
                length = right - left + 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
