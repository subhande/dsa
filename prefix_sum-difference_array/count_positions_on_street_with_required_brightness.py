# Count Positions on Street With Required Brightness

from typing import List

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        brightness = [0] * n

        for light in lights:
            position, lrange = light
            start = max(0, position-lrange)
            end = min(n-1, position+lrange)
            brightness[start] += 1
            if end + 1 < n:
                brightness[end+1] += -1

        count = 0

        for i in range(n):
            if i != 0:
                brightness[i] += brightness[i-1]
            if brightness[i] >= requirement[i]:
                count += 1

        return count
