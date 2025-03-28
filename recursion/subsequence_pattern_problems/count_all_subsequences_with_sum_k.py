# Count all subsequences with sum K


class Solution:
    def countSubsequenceWithTargetSumRecursive(self, nums, k, currSum, index):
        if currSum == 0:
            return 1
        if index == 0:
            return 1 if nums[index] == currSum else 0
        return self.countSubsequenceWithTargetSumRecursive(nums, k, currSum - nums[index], index - 1) + self.countSubsequenceWithTargetSumRecursive(nums, k, currSum, index - 1)

    def countSubsequenceWithTargetSum(self, nums, k):
        return self.countSubsequenceWithTargetSumRecursive(nums, k, k, len(nums)-1)


class SolutionMemo:
    def countSubsequenceWithTargetSumRecursive(self, nums, k, currSum, index, memo):
        if currSum == 0:
            return 1
        if index == 0:
            return 1 if nums[index] == currSum else 0
        if (currSum, index) in memo:
            return memo[(currSum, index)]
        memo[(currSum, index)] = self.countSubsequenceWithTargetSumRecursive(nums, k, currSum - nums[index], index - 1, memo) + self.countSubsequenceWithTargetSumRecursive(nums, k, currSum, index - 1, memo)
        return memo[(currSum, index)]

    def countSubsequenceWithTargetSum(self, nums, k):
        return self.countSubsequenceWithTargetSumRecursive(nums, k, k, len(nums)-1, {})
