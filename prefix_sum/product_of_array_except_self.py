# Product of array except self
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProductArray = [1] * (n+1)
        product = 1
        for idx in range(n):
            product *= nums[idx]
            prefixProductArray[idx] = product

        suffixProductArray = [1] * n
        product = 1
        for idx in range(n-1, -1, -1):
            product *= nums[idx]
            suffixProductArray[idx] = product

        result = [1] * n
        for idx in range(n):
            if idx == 0:
                result[idx] = suffixProductArray[idx+1]
            elif idx == n - 1:
                result[idx] = prefixProductArray[idx-1]
            else:
                result[idx] = prefixProductArray[idx-1] * suffixProductArray[idx+1]
        return result
