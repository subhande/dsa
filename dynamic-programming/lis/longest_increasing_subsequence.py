# Longest Increasing Subsequence
from typing import List

class Solution:
    def LISRecursiveMemo(self, nums: List[int], prev: int, curr: int, memo: List) -> int:
        if curr == len(nums):
            return 0
        if memo[curr][prev + 1] != -1:
            return memo[curr][prev + 1]
        not_taken = self.LISRecursiveMemo(nums, prev, curr + 1, memo)
        taken = 0
        if prev == -1 or nums[curr] > nums[prev]:
            taken = 1 + self.LISRecursiveMemo(nums, curr, curr + 1, memo)
        memo[curr][prev + 1] = max(taken, not_taken)
        return memo[curr][prev + 1]
    def LIS(self, nums: List[int]) -> int:
        memo = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        return self.LISRecursiveMemo(nums, -1, 0, memo)



class Solution2:
    def LISTabularSpaceOptimized(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    nums = [1,3,5,4,7]
    print(Solution().LIS(nums)) # Output 4
    print(Solution2().LISTabularSpaceOptimized(nums)) # Output 4
