# Combination Sum II

from typing import List

class Solution:
    def combinationSumRecursive(self, candidates, target, index, currCombination):
        if target == 0:
            return [currCombination]
        if index == 0:
            if target == candidates[index]:
                currCombination = [candidates[index]] + currCombination
                return [currCombination]
            return []
        taken = []
        notTaken = []
        if target >= candidates[index]:
            taken = self.combinationSumRecursive(candidates, target-candidates[index], index-1, [candidates[index]] + currCombination)
        # Skip duplicates: if not picking the current candidate,
        # ensure the next candidate is different
        for nextIndex in range(index - 1, -1 , -1):
            if candidates[nextIndex] != candidates[index]:
                notTaken = self.combinationSumRecursive(candidates, target, nextIndex, currCombination[:])
                break
        return taken + notTaken
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        validCombinations = self.combinationSumRecursive(candidates, target, len(candidates) - 1, [])
        return validCombinations

class Solution2:
    def combinationSumRecursive(self, candidates, target, index, currCombination):
        if target == 0:
            return [currCombination]
        if index == 0:
            if target == candidates[index]:
                currCombination = [candidates[index]] + currCombination
                return [currCombination]
            return []
        taken = []
        notTaken = []
        if target >= candidates[index]:
            taken = self.combinationSumRecursive(candidates, target-candidates[index], index-1, [candidates[index]] + currCombination)
        # Skip duplicates: if not picking the current candidate,
        # ensure the next candidate is different
        for nextIndex in range(index - 1, -1 , -1):
            if candidates[nextIndex] != candidates[index]:
                notTaken = self.combinationSumRecursive(candidates, target, nextIndex, currCombination[:])
                break
        return taken + notTaken
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        validCombinations = self.combinationSumRecursive(candidates, target, len(candidates) - 1, [])
        return validCombinations
