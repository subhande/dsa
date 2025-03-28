# Check if there exists a subsequence with sum K

class Solution:
    def checkSubsequenceSumRecursive(self, nums, k, currSum, index):
        if currSum == 0:
            return True
        if index == 0:
            return True if nums[index] == currSum else False
        return self.checkSubsequenceSumRecursive(nums, k, currSum - nums[index], index - 1) or self.checkSubsequenceSumRecursive(nums, k, currSum, index - 1)

    def checkSubsequenceSum(self, nums, k):
        return self.checkSubsequenceSumRecursive(nums, k, k, len(nums)-1)


class SolutionMemo:
    def checkSubsequenceSumRecursive(self, nums, k, currSum, index, memo):
        if currSum == 0:
            return True
        if index == 0:
            return True if nums[index] == currSum else False
        if (currSum, index) in memo:
            return memo[(currSum, index)]
        memo[(currSum, index)] = self.checkSubsequenceSumRecursive(nums, k, currSum - nums[index], index - 1, memo) or self.checkSubsequenceSumRecursive(nums, k, currSum, index - 1, memo)
        return memo[(currSum, index)]

    def checkSubsequenceSum(self, nums, k):
        return self.checkSubsequenceSumRecursive(nums, k, k, len(nums)-1, {})
