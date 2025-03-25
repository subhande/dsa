
# Largest Divisble Subset


from typing import List
class Solution:
    def largestDivisibleSubsetRecursiveMemo(self, nums: List[int], prev: int, curr: int, memo: List) -> list:
        if curr == len(nums):
            return []
        if memo[curr][prev + 1] != -1:
            return memo[curr][prev + 1]
        not_taken = self.largestDivisibleSubsetRecursiveMemo(nums, prev, curr + 1, memo)
        taken = []
        if prev == -1 or nums[curr] % nums[prev] == 0 or nums[prev] % nums[curr] == 0:
            taken = [nums[curr]] + self.largestDivisibleSubsetRecursiveMemo(nums, curr, curr + 1, memo)
        memo[curr][prev + 1] = taken if len(taken) > len(not_taken) else not_taken
        return memo[curr][prev + 1]
    def largestDivisibleSubset(self, nums: List[int]) -> list:
        memo = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        if not nums:
            return []
        nums.sort()
        subsequence = self.largestDivisibleSubsetRecursiveMemo(nums, -1, 0, memo)
        return subsequence
