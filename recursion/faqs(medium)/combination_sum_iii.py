# Combination Sum III

from typing import List

class Solution:
    def combinationSum3Recursive(self, k: int, n: int, index: int, nums: list, currCombination: list, validCombinations: list):
        if n == 0:
            if k == 0:
                validCombinations.append(currCombination)
            return
        if index == 0:
            if k == 1 and n == nums[index]:
                validCombinations.append([nums[index]] + currCombination)
            return
        self.combinationSum3Recursive(k, n, index-1, nums, currCombination[:], validCombinations)
        self.combinationSum3Recursive(k-1, n-nums[index], index-1, nums, [nums[index]] + currCombination, validCombinations)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        validCombinations = []
        self.combinationSum3Recursive(k, n, len(nums)-1, nums, [], validCombinations)
        return validCombinations
