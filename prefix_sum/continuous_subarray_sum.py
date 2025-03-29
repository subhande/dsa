# Continuous Subarray Sum
#
from typing import List
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashMap = defaultdict(int)
        hashMap[0] = -1
        sumSoFar = 0
        for index in range(n):
            sumSoFar += nums[index]
            mod = sumSoFar % k
            if mod in hashMap:
                if index - hashMap[mod] > 1:
                    return True
            else:
                hashMap[mod] = index
        return False

class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashMap = defaultdict(int)
        hashMap[0] = -1
        sumSoFar = 0
        for index in range(n):
            sumSoFar += nums[index]
            mod = sumSoFar % k
            if mod not in hashMap:
                hashMap[mod] = index
            elif index - hashMap[mod] > 1:
                return True
        return False
