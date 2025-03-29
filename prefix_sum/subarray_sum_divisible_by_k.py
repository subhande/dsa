# Subarray Sum Divisible by K

from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod = 0
        result = 0
        # // There are k mod groups 0...k-1.
        modGroups = defaultdict(int)
        modGroups[0] = 1
        for num in nums:
            # // Take modulo twice to avoid negative remainders.
            prefixMod = (prefixMod + num % k + k) % k
            # print(["before", num, modGroups, result])
            # // Add the count of subarrays that have the same remainder as the current
            # // one to cancel out the remainders.
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1
            # print(["after", num, modGroups, result])

        return result


class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod = 0
        sum = 0
        result = 0
        # // There are k mod groups 0...k-1.
        modGroups = defaultdict(int)
        modGroups[0] = 1
        for num in nums:
            sum += num
            prefixMod = sum % k
            # // Take modulo twice to avoid negative remainders.
            # prefixMod = (prefixMod + num % k + k) % k
            # print(["before", num, modGroups, result])
            # // Add the count of subarrays that have the same remainder as the current
            # // one to cancel out the remainders.
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1
            # print(["after", num, modGroups, result])

        return result
