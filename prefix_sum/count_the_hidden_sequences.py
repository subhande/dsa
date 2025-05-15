# Count the hidden sequences
# https://leetcode.com/problems/count-the-hidden-sequences/description
from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        maxPositiveDelta = 0
        minNegativeDelta = 0

        prefixSum = 0

        for diff in differences:
            prefixSum += diff
            maxPositiveDelta = max(maxPositiveDelta, prefixSum)
            minNegativeDelta = min(minNegativeDelta, prefixSum)
        nonOfSequences = (upper-maxPositiveDelta) - (lower - minNegativeDelta) + 1

        return nonOfSequences if nonOfSequences > 0 else 0
