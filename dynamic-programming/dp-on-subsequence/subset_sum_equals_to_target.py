# Subset sum equals to target
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        prev = [False] * (target + 1)

        prev[0] = True

        if arr[0] <= target:
            prev[arr[0]] = True

        for ind in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for i in range(1, target + 1):
                notTaken = prev[i]
                taken = False
                if arr[ind] <= i:
                    taken = prev[i - arr[ind]]
                curr[i] = notTaken or taken
            prev = curr[:]
        return prev[target]


class Solution2:
    """ Function to check if there is a subset of arr
    with sum equal to 'target' using memoization"""
    def func(self, ind, target, arr, dp):
        # Base cases
        if target == 0:
            return True

        if ind == 0:
            return arr[0] == target

        """ Check if the result for this combination of
        'ind' and 'target' has already been computed"""
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Try not taking the current element into subset
        notTaken = self.func(ind - 1, target, arr, dp)

        """ Try taking the current element into the
        subset if it doesn't exceed the target"""
        taken = False
        if arr[ind] <= target:
            taken = self.func(ind - 1, target - arr[ind], arr, dp)

        # Return the result
        return notTaken or taken

    """ Function to check if there is a subset
    of 'arr' with sum equal to 'target'"""
    def isSubsetSum(self, arr, target):
        # Initialize a memoization table with -1.
        dp = [[-1 for j in range(target + 1)] for i in range(len(arr))]

        # Return the result
        return self.func(len(arr) - 1, target, arr, dp)
