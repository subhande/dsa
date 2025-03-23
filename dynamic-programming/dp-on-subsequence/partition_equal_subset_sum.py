# Partition Equal Subset Sum

class Solution:
    """ Function to check if it's possible to partition
    the array into two subsets with equal sum"""
    def func(self, n, arr):
        tot_sum = 0

        # Calculate the total sum of the array
        for i in range(n):
            tot_sum += arr[i]

        """ If the total sum is odd, it cannot
        be partitioned into two equal subsets"""
        if tot_sum % 2 == 1:
            return False
        else:
            k = tot_sum // 2

            """ Initialize a vector to represent the
            previous row of the DP table"""
            prev = [False] * (k + 1)
            prev[0] = True

            """ Initialize the first row based
            on the first element of the array"""
            if arr[0] <= k:
                prev[arr[0]] = True

            # Fill in the DP table using a bottom-up approach
            for ind in range(1, n):
                """ Initialize a vector to represent
                the current row of the DP table"""
                cur = [False] * (k + 1)
                cur[0] = True

                for target in range(1, k + 1):
                    # Exclude the current element
                    not_taken = prev[target]

                    """ Include the current element
                    if it doesn't exceed the target"""
                    taken = False
                    if arr[ind] <= target:
                        taken = prev[target - arr[ind]]

                    # Update the current row of the DP table
                    cur[target] = not_taken or taken

                """ Set the current row as the
                previous row for the next iteration"""
                prev = cur

            """ The final result is in the last cell
            of the previous row of the DP table"""
            return prev[k]

    """ Function to check if the array can
    be partitioned into two equal subsets"""
    def equalPartition(self, n, arr):
        # Return the result
        return self.func(n, arr)
