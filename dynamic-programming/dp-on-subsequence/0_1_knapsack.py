# 0-1 KnapSack

class Solution:
    # Function to solve the 0/1 Knapsack problem
    def knapsack01(self, wt, val, n, W):
        """ Initialize a vector 'prev' to represent
        the previous row of the DP table"""
        prev = [0] * (W + 1)

        """ Base condition: Fill in 'prev'
        for the weight of the first item"""
        for i in range(wt[0], W + 1):
            prev[i] = val[0]

        # Fill in the table using a bottom-up approach
        for ind in range(1, n):
            for cap in range(W, -1, -1):
                """ Calculate the maximum value by either
                excluding the current item or including it"""
                notTaken = prev[cap]
                taken = float('-inf')

                """ Check if the current item can be included
                without exceeding the knapsack's capacity"""
                if wt[ind] <= cap:
                    taken = val[ind] + prev[cap - wt[ind]]

                # Update 'prev' for the current capacity
                prev[cap] = max(notTaken, taken)

        """ The final result is in the
        last cell of the 'prev' vector"""
        return prev[W]


class Solution2:
    # Function to solve the 0/1 Knapsack problem with arrays
    def func(self, wt, val, ind, W, dp):
        """ Base case: If there are no items left
        or the knapsack has no capacity, return 0"""
        if ind < 0 or W == 0:
            return 0

        """ If the result for this state is
        already calculated, return it"""
        if dp[ind][W] != -1:
            return dp[ind][W]

        """ Calculate the maximum value by either
        excluding the current item or including it"""
        not_taken = self.func(wt, val, ind - 1, W, dp)
        taken = 0

        """ Check if the current item can be included
        without exceeding the knapsack's capacity"""
        if wt[ind] <= W:
            taken = val[ind] + self.func(wt, val, ind - 1, W - wt[ind], dp)

        # Store the result in the DP table and return
        dp[ind][W] = max(not_taken, taken)
        return dp[ind][W]

    def knapsack01(self, wt, val, n, W):
        # Initialize DP table with -1
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.func(wt, val, n - 1, W, dp)
