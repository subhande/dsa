"""
Unbounded Knapsack Problem
--------------------------

Given two integer arrays, val and wt, each of size N, representing the values and weights of N items respectively, and an integer W, representing the maximum capacity of a knapsack, determine the maximum value achievable by selecting a subset of the items such that the total weight of the selected items does not exceed the knapsack capacity W. The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity. An infinite supply of each item can be assumed.


Examples:
Input: val = [5, 11, 13], wt = [2, 4, 6], W = 10
Output: 27

Explanation: Select 2 items with weights 4 and 1 item with weight 2 for a total value of 11+11+5 = 27.

Input: val = [10, 40, 50, 70], wt = [1, 3, 4, 5], W = 8
Output: 110

Explanation: Select items with weights 3 and 5 for a total value of 40 + 70 = 110.


Constraints:
1 ≤ N ≤ 500
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 500
1 ≤ val[i] ≤ 500
    
"""


class Solution:

    ################################
    # Recursive Approach
    ################################
    def unboundedKnapsackRecursiveHelper(self, weights, values, index, capacity):
        """
        Helper function for the recursive approach.
        Calculates the maximum value for a given index and remaining capacity.
        """
        if index == 0:
            # Base case: If only one item is considered, use it as much as possible
            return (capacity // weights[0]) * values[0]

        # Option 1: Do not take the current item
        maxValueWithoutItem = self.unboundedKnapsackRecursiveHelper(weights, values, index - 1, capacity)

        # Option 2: Take the current item (if its weight allows it)
        maxValueWithItem = 0
        if weights[index] <= capacity:
            maxValueWithItem = values[index] + self.unboundedKnapsackRecursiveHelper(
                weights, values, index, capacity - weights[index]
            )

        return max(maxValueWithoutItem, maxValueWithItem)

    def unboundedKnapsackRecursive(self, weights, values, n, capacity):
        """
        Wrapper function for the recursive approach.
        """
        return self.unboundedKnapsackRecursiveHelper(weights, values, n - 1, capacity)

    ################################
    # Memoization Approach
    ################################
    def unboundedKnapsackMemoizationHelper(self, weights, values, index, capacity, memo):
        """
        Helper function for the memoization approach.
        Uses a memo table to store previously computed results.
        """
        if index == 0:
            return (capacity // weights[0]) * values[0]

        if memo[index][capacity] != -1:
            return memo[index][capacity]

        # Option 1: Do not take the current item
        maxValueWithoutItem = self.unboundedKnapsackMemoizationHelper(weights, values, index - 1, capacity, memo)

        # Option 2: Take the current item (if its weight allows it)
        maxValueWithItem = 0
        if weights[index] <= capacity:
            maxValueWithItem = values[index] + self.unboundedKnapsackMemoizationHelper(
                weights, values, index, capacity - weights[index], memo
            )

        memo[index][capacity] = max(maxValueWithoutItem, maxValueWithItem)
        return memo[index][capacity]

    def unboundedKnapsackMemoization(self, weights, values, n, capacity):
        """
        Memoization approach to solve the unbounded knapsack problem.
        """
        memo = [[-1 for _ in range(capacity + 1)] for _ in range(n)]
        return self.unboundedKnapsackMemoizationHelper(weights, values, n - 1, capacity, memo)

    ################################
    # Tabulation Approach
    ################################
    def unboundedKnapsackTabulation(self, weights, values, n, capacity):
        """
        Tabulation approach to solve the unbounded knapsack problem.
        Builds a bottom-up DP table to compute the solution iteratively.
        """
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

        # Fill the first row for using the first item
        for cap in range(weights[0], capacity + 1):
            dp[0][cap] = (cap // weights[0]) * values[0]

        # Build the DP table
        for index in range(1, n):
            for cap in range(capacity + 1):
                maxValueWithoutItem = dp[index - 1][cap]
                maxValueWithItem = 0
                if weights[index] <= cap:
                    maxValueWithItem = values[index] + dp[index][cap - weights[index]]
                dp[index][cap] = max(maxValueWithoutItem, maxValueWithItem)

        return dp[n - 1][capacity]

    ################################
    # Tabulation Space Optimized Approach
    ################################
    def unboundedKnapsackTabulationSpaceOptimized(self, weights, values, n, capacity):
        """
        Space-optimized tabulation approach to solve the unbounded knapsack problem.
        Reduces space complexity by using only two 1D arrays.
        """
        prev = [0] * (capacity + 1)

        # Fill the first row for using the first item
        for cap in range(weights[0], capacity + 1):
            prev[cap] = (cap // weights[0]) * values[0]

        # Update the DP array for each item
        for index in range(1, n):
            curr = [0] * (capacity + 1)
            for cap in range(capacity + 1):
                maxValueWithoutItem = prev[cap]
                maxValueWithItem = 0
                if weights[index] <= cap:
                    maxValueWithItem = values[index] + curr[cap - weights[index]]
                curr[cap] = max(maxValueWithoutItem, maxValueWithItem)
            prev = curr[:]

        return prev[capacity]


if __name__ == "__main__":
    # Create an instance of Solution class
    sol = Solution()

    # Test cases
    test_cases = [
        {"weights": [2, 4, 6], "values": [5, 11, 13], "capacity": 10, "expected": 27},
        {"weights": [1, 3, 4, 5], "values": [10, 40, 50, 70], "capacity": 8, "expected": 110},
    ]

    for test in test_cases:
        weights = test["weights"]
        values = test["values"]
        capacity = test["capacity"]
        expected = test["expected"]
        n = len(weights)

        print("=" * 50)
        print("The maximum value is (Recursive):", sol.unboundedKnapsackRecursive(weights, values, n, capacity))
        print("The maximum value is (Memoization):", sol.unboundedKnapsackMemoization(weights, values, n, capacity))
        print("The maximum value is (Tabulation):", sol.unboundedKnapsackTabulation(weights, values, n, capacity))
        print(
            "The maximum value is (Space Optimized):",
            sol.unboundedKnapsackTabulationSpaceOptimized(weights, values, n, capacity),
        )
        print("Expected:", expected)
