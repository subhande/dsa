from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        currentElement = nums[0]
        currentElementCount = 1
        for idx in range(1, len(nums)):
            if currentElement == nums[idx] and currentElementCount >= 2:
                currentElementCount += 1
                continue
            elif currentElement == nums[idx]:
                currentElementCount += 1
                nums[insertIndex] = nums[idx]
                insertIndex += 1
            else:
                currentElement = nums[idx]
                currentElementCount = 1
                nums[insertIndex] = nums[idx]
                insertIndex += 1
        return insertIndex
