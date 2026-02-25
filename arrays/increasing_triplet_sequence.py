# Increasing Triplet Subsequence
from typing import List


# Approach 1: Brute Force
# Time Complexity: O(n^3) | Space Complexity: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        return False

# Approach 2: Optimal Solution
# Time Co# Time Complexity: O(n) | Space Complexity: O(1)
class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_number = float('inf')
        second_smallest_number = float('inf')

        for num in nums:
            if num <= smallest_number:
                smallest_number = num
            elif num <= second_smallest_number:
                second_smallest_number = num
            else:
                return True
        return False
n False
