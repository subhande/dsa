# Subset II

class Solution:
    def subsetSumsRecursive(self, nums, index, currSubset, validSubset):
        if index == -1:
            validSubset.append(currSubset)
            return
        self.subsetSumsRecursive(nums, index-1, [nums[index]] + currSubset, validSubset)
        # Skip duplicates and recur for the next unique element
        for nextNext in range(index-1, -1, -1):
            if nums[nextNext] != nums[index]:
                self.subsetSumsRecursive(nums, nextNext, currSubset[:], validSubset)
                return
        # Ensure the function finishes when no more unique elements are left
        self.subsetSumsRecursive(nums, -1, currSubset[:], validSubset)

    def subsetsWithDup(self, nums):
        validSubset = []
        nums.sort()
        self.subsetSumsRecursive(nums, len(nums)-1, [], validSubset)
        return validSubset
