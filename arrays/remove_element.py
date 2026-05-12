from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
