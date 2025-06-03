# Contiguous Array

from typing import List

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumSoFar = 0
        maxValidArraySize = 0
        hashMap = defaultdict(int)
        hashMap[0] = -1
        for index in range(len(nums)):
            sumSoFar += -1 if nums[index] == 0 else 1

            if sumSoFar in hashMap:
                maxValidArraySize = max(maxValidArraySize, index - hashMap[sumSoFar])
            else:
                hashMap[sumSoFar] = index
        return maxValidArraySize
