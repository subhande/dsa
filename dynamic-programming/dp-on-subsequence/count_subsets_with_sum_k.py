# Count subsets with sum K

MODULO = 10**9 + 7

class Solution:
    # Function to find out number of subsets with sum k
    def perfectSum(self, arr, K):
        n = len(arr)

        """ Initialize a vector 'prev' to represent
        the previous row of the DP table"""
        prev = [0] * (K + 1)

        """ Base case: If the target sum is 0,
        there is one valid subset (the empty subset)"""
        prev[0] = 1

        """ Initialize the first row based
        on the first element of the array"""
        if arr[0] <= K:
            prev[arr[0]] = 1

        """ Fill in the DP table
        using a bottom-up approach"""
        for ind in range(1, n):
            """ Create a vector 'cur' to represent
            the current row of the DP table"""
            cur = [0] * (K + 1)

            cur[0] = 1

            for target in range(1, K + 1):
                # Exclude the current element
                notTaken = prev[target]

                """ Include the current element
                if it doesn't exceed the target"""
                taken = 0
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]

                # Update the current row of the DP table
                cur[target] = (notTaken + taken) % MODULO

            # Set 'cur' as 'prev' for the next iteration
            prev = cur

        """ The final result is in the
        last cell of the 'prev' vector"""
        return prev[K]


MODULO = 10**9 + 7

class Solution2:
    """ Function to count the number of
    subsets with sum k using memoization """
    def findWaysUtil(self, ind, target, arr, dp):
        """ Base case: If the target sum
        is 0, we found a valid subset """
        if target == 0:
            return 1

        """ Base case: If we have considered all elements
        and the target is still not 0, return 0 """
        if ind == 0:
            return 1 if arr[0] == target else 0

        """ If the result for this state
        is already calculated, return it """
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Exclude the current element
        notTaken = self.findWaysUtil(ind - 1, target, arr, dp)

        """ Include the current element if
        it doesn't exceed the target"""
        taken = 0
        if arr[ind] <= target:
            taken = self.findWaysUtil(ind - 1, target - arr[ind], arr, dp)

        """Store the result in DP table and return
        Also, take modulo for the code to be accepted"""
        dp[ind][target] = (notTaken + taken) % MODULO
        return dp[ind][target]

    # Function to find out number of subsets with sum k
    def perfectSum(self, arr, K):
        n = len(arr)

        # DP array to store the subproblems
        dp = [[-1] * (K + 1) for _ in range(n)]

        # Return the result
        return self.findWaysUtil(n - 1, K, arr, dp)
