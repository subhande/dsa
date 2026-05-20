# Squares of a Sorted Array
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                ele = nums[right]
                right -= 1
            else:
                ele = nums[left]
                left += 1
            result[i] = ele * ele
        return result


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        idx = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = abs(nums[left]) * abs(nums[left])
                left += 1
                idx -= 1
            else:
                result[idx] = abs(nums[right]) * abs(nums[right])
                right -= 1
                idx -= 1

        return result
