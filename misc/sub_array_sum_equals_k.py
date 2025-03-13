# Sub Array Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List

class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for start in range(n):
            sum = 0
            for end in range(start, n):
                sum += nums[end]
                if sum == k:
                    count += 1
        return count

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        hashMap = {0: 1}
        sum = 0
        for start in range(n):
            sum += nums[start]
            if sum - k in hashMap:
                count += hashMap.get(sum - k, 0)
            hashMap[sum] = hashMap.get(sum, 0) + 1
        return count
