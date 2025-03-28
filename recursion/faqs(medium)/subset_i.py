# Subset I

class Solution:
    def subsetSumsRecursive(self, nums, index, currSum, validSubset):
        if index == -1:
            validSubset.append(currSum)
            return
        self.subsetSumsRecursive(nums, index-1, currSum + nums[index], validSubset)
        self.subsetSumsRecursive(nums, index-1, currSum, validSubset)

    def subsetSums(self, nums):
        validSubset = []
        self.subsetSumsRecursive(nums, len(nums)-1, 0, validSubset)
        return validSubset
