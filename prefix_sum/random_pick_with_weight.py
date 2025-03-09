# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/description/?envType=problem-list-v2&envId=prefix-sum

from typing import List
import random

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



if __name__ == '__main__':
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
