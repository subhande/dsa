# Range Addition

from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        differenceArray = [0] * length

        for update in updates:
            differenceArray[update[0]] += update[2]
            if update[1]+1 < length:
                differenceArray[update[1]+1] += -1 * update[2]

        for i in range(1, length):
            differenceArray[i] += differenceArray[i-1]

        return differenceArray
