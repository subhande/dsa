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
