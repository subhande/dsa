# Search in Rotated Sorted Array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            # Case 1: Find target
            if nums[mid] == target:
                return mid
            # Case 2: Left subarray is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target  and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Case 3: Right is sorted
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
