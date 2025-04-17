# Partition a set into two subsets with minimum absolute sum difference

class Solution:
    """ Function to find the minimum absolute
    difference between two subset sums"""
    def minDifference(self, arr, n):
        totSum = sum(arr)

        """ Initialize a boolean vector 'prev' to
        represent the previous row of the DP table"""
        prev = [False] * (totSum + 1)
        prev[0] = True

        """ Initialize the first row based
        on the first element of the array"""
        if arr[0] <= totSum:
            prev[arr[0]] = True

        # Fill in the DP table using bottom-up approach
        for ind in range(1, n):
            """ Initialize a boolean vector 'cur' to
            represent the current row of the DP table"""
            cur = [False] * (totSum + 1)
            cur[0] = True

            for target in range(1, totSum + 1):
                # Exclude the current element
                notTaken = prev[target]

                """ Include the current element if
                it doesn't exceed the target"""
                taken = False
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]

                cur[target] = notTaken or taken

            # Set 'cur' as the 'prev' for the next iteration
            prev = cur

        mini = float('inf')
        for i in range(totSum + 1):
            if prev[i]:
                """ Calculate the absolute
                difference between two subset sums"""
                diff = abs(i - (totSum - i))
                mini = min(mini, diff)

        return mini


class Solution2:
    # Function to solve the subset sum problem
    def func(self, ind, target, arr, dp):
        # Base case: If the target sum is 0, return true
        if target == 0:
            dp[ind][target] = True
            return True

        """ Base case: If we have considered all elements
        and the target is still not 0, return false"""
        if ind == 0:
            dp[ind][target] = (arr[0] == target)
            return dp[ind][target]

        """ If the result for this state is
        already calculated, return it"""
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Exclude the current element
        not_taken = self.func(ind - 1, target, arr, dp)

        """ Include the current element if
        it doesn't exceed the target"""
        taken = False
        if arr[ind] <= target:
            taken = self.func(ind - 1, target - arr[ind], arr, dp)

        # Return the result
        dp[ind][target] = not_taken or taken
        return dp[ind][target]

    """ Function to find the minimum absolute
    difference between two subset sums"""
    def minDifference(self, arr, n):
        tot_sum = 0

        # Calculate the total sum of the array
        for i in range(n):
            tot_sum += arr[i]

        """ Initialize a DP table to store the
        results of the subset sum problem"""
        dp = [[-1 for _ in range(tot_sum + 1)] for _ in range(n)]

        """ Calculate the subset sum for each
        possible sum from 0 to the total sum"""
        for i in range(tot_sum + 1):
            self.func(n - 1, i, arr, dp)


        mini = float('inf')
        for i in range(tot_sum + 1):
            if dp[n - 1][i] == True:
                diff = abs(i - (tot_sum - i))
                mini = min(mini, diff)

        return mini


if __name__ == "__main__":
    arr = [1, 7, 14, 5]
    n = len(arr)
    sol = Solution()
    print(sol.minDifference(arr, n))  # Output: 1
    sol2 = Solution2()
    print(sol2.minDifference(arr, n))  # Output: 1
