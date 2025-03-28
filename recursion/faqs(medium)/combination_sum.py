# Combination Sum

from typing import List

class Solution:
    def combinationSumRecursive(self, candidates, target, index, currCombination, validCombinations):
        if target == 0:
            validCombinations.append(currCombination)
            return
        # Either we can go with index == 0 or we can go with index == -1
        if index == 0:
            if target % candidates[index] == 0:
                temp = [candidates[index]] * (target // candidates[index])
                target = 0
                currCombination.extend(temp)
                validCombinations.append(currCombination)
            return
        # if index == -1:
        #     return
        self.combinationSumRecursive(candidates, target, index-1, currCombination[:], validCombinations)
        if target >= candidates[index]:
            self.combinationSumRecursive(candidates, target-candidates[index], index, currCombination + [candidates[index]], validCombinations)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        validCombinations = []
        self.combinationSumRecursive(candidates, target, len(candidates) - 1, [], validCombinations)
        return validCombinations


class Solution2:
    class Solution:
        def combinationSumRecursive(self, candidates, target, index, currCombination):
            if target == 0:
                return [currCombination]
            if index == 0:
                if target % candidates[index] == 0:
                    temp = [candidates[index]] * (target // candidates[index])
                    target = 0
                    currCombination = temp + currCombination
                    return [currCombination]
                return []
            taken = []
            if target >= candidates[index]:
                taken = self.combinationSumRecursive(candidates, target-candidates[index], index, [candidates[index]] + currCombination)
            notTaken = self.combinationSumRecursive(candidates, target, index-1, currCombination[:])
            return taken + notTaken
        def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            validCombinations = self.combinationSumRecursive(candidates, target, len(candidates) - 1, [])
            return validCombinations
