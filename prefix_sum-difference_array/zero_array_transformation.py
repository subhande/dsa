# Zero Array Transformation

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        differenceArray = [0] * n

        for query in queries:
            differenceArray[query[0]] += 1
            if query[1] + 1 < n:
                differenceArray[query[1]+1] += -1
        for i in range(1, n):
            differenceArray[i] += differenceArray[i-1]

        for i in range(n):
            nums[i] = max(nums[i]-differenceArray[i], 0)


        return sum(nums) == 0
