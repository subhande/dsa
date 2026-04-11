# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/description/?envType=problem-list-v2&envId=prefix-sum
# Ref: https://youtu.be/fWS0TCcr-lE
import random
from typing import List

"""

w = [1, 2, 3, 4]

-- | -- -- | -- -- -- | -- -- -- -- |
   1       3          6            10

prefixSum = 10
target = 10 * random.random()  # target is a random number between 0 and 10
       = 2.5
target is in the range of 1 and 3, so we return index 1
So we represent all sums as zones on a number line, and we pick a random number in the range of the total sum. The zone in which the random number falls corresponds to the index we return.

"""


class Solution1:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
        return -1


class Solution2:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = (low + high) // 2
            # mid = low + (high - low) // 2 avoids that potential issue because it first computes the difference between high and low, which is guaranteed not to overflow (assuming high is greater than or equal to low), and then adds low back after dividing by two.
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == "__main__":
    w = [1, 3]
    obj = Solution1(w)
    print(obj.pickIndex())

    obj = Solution2(w)
    print(obj.pickIndex())

    w = [1, 3, 4, 5]

    obj = Solution1(w)
    print(obj.pickIndex())

    obj = Solution2(w)
    print(obj.pickIndex())
