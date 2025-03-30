# Minumum Bit Flip To Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        count = 0
        while result:
            result = result & result-1
            count += 1
        return count
