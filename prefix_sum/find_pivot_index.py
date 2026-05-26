from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i - 1]

        for i in range(n):
            if i == 0:
                if nums[-1] - nums[0] == 0:
                    return 0
            else:
                if nums[-1] - nums[i] == nums[i - 1]:
                    return i
        return -1
