# Range Addition

from typing import List


# Time Complexity: O(n + k) where n is the length of the array and k is the number of updates | Space Complexity: O(n) where n is the length of the array
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        differenceArray = [0] * length

        for update in updates:
            differenceArray[update[0]] += update[2]
            if update[1] + 1 < length:
                differenceArray[update[1] + 1] += -1 * update[2]

        for i in range(1, length):
            differenceArray[i] += differenceArray[i - 1]

        return differenceArray


class Solution2:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length

        for update in updates:
            arr[update[0]] += update[-1]
            if update[1] + 1 < length:
                arr[update[1] + 1] += -1 * update[-1]

        for i in range(1, length):
            arr[i] += arr[i - 1]

        return arr
