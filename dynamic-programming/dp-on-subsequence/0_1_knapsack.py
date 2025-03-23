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
