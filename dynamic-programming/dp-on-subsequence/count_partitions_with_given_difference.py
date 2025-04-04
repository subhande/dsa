# Count partitions with given difference

class Solution:
    # Modulus value to avoid overflow in calculations.
    mod = int(1e9 + 7)

    """Function to calculate the number of subsets
       with a specific target sum. Uses space optimization
       to store only the previous state in the DP table."""
    def findWays(self, num, tar):
        n = len(num)

        """ DP table to store number of ways
        to achieve a certain target sum."""
        prev = [0] * (tar + 1)

        """ 2 cases for target 0 when the first
        element is 0: either pick it or not."""
        if num[0] == 0:
            prev[0] = 2

        else:
            prev[0] = 1

        """ Initialize the base case for the
        first element and non-zero target."""
        if num[0] != 0 and num[0] <= tar:
            prev[num[0]] = 1

        """ Iterate through all elements of the
        array starting from the second element."""
        for ind in range(1, n):
            cur = [0] * (tar + 1)
            for target in range(tar + 1):
                """ Number of ways to achieve the target
                sum without including the current element."""
                not_taken = prev[target]

                """ Number of ways to achieve the target sum
                by including the current element."""
                taken = 0
                if num[ind] <= target:
                    taken = prev[target - num[ind]]

                """ Total ways to achieve the target sum either
                including or excluding the current element."""
                cur[target] = (not_taken + taken) % Solution.mod

            """ Update the previous state to the
            current state for the next iteration."""
            prev = cur

        # Return the number of subsets
        return prev[tar]

    def countPartitions(self, n, diff, arr):
        tot_sum = sum(arr)

        # Checking for edge cases
        if tot_sum - diff < 0 or (tot_sum - diff) % 2:
            return 0

        # Calculate the target sum for one subset.
        return self.findWays(arr, (tot_sum - diff) // 2)



class Solution2:
    # Modulus value to avoid overflow in calculations.
    mod = int(1e9 + 7)

    def countPartitionsUtil(self, ind, target, arr, dp):
        # Base case: If we are at the first element.
        if ind == 0:
            """ If target is 0 and element is also 0, there
            are 2 ways to achieve this (include or exclude)."""
            if target == 0 and arr[0] == 0:
                return 2
            """ If target is 0 or the element is equal to
            target, there is 1 way to achieve this."""
            if target == 0 or target == arr[0]:
                return 1
            return 0

        # Return the result if it has already been computed.
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Calculate number of ways not including current element.
        not_taken = self.countPartitionsUtil(ind - 1, target, arr, dp)

        """ Calculate the number of ways including
        the current element (if it can be included)."""
        taken = 0
        if arr[ind] <= target:
            taken = self.countPartitionsUtil(ind - 1, target - arr[ind], arr, dp)

        # Store and return the result for the current subproblem.
        dp[ind][target] = (not_taken + taken) % self.mod
        return dp[ind][target]

    def countPartitions(self, n, diff, arr):
        tot_sum = sum(arr)

        """If the total sum minus the difference is negative,
        or if it is not even, it's not possible to divide
        the array into two subsets with the given difference."""
        if tot_sum - diff < 0 or (tot_sum - diff) % 2 == 1:
            return 0

        # Calculate the target sum for one of the subsets.
        s2 = (tot_sum - diff) // 2

        # Initialize the DP table with -1 for memoization.
        dp = [[-1 for _ in range(s2 + 1)] for _ in range(n)]

        """ Call the helper function to count
        the number of subsets with sum s2."""
        return self.countPartitionsUtil(n - 1, s2, arr, dp)
