# Counting Bits
# https://leetcode.com/problems/counting-bits/description/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_counts = [0]
        for i in range(1, n+1):
            num = i
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            bit_counts.append(count)
        return bit_counts
