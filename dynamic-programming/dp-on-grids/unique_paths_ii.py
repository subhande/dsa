# Unique Paths II
# https://takeuforward.org/plus/dsa/dynamic-programming/dp-on-grids/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n
        for j in range(n):
            if matrix[0][j] == 1:
                break
            dp[j] = 1
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] if matrix[i][j] != 1 else 0
                else:
                    dp[j] = dp[j-1] + dp[j] if matrix[i][j] != 1 else 0
        return dp[-1]

class Solution2:
    # Function to solve the problem using memoization
    def func(self, i, j, matrix, dp):
        # Base cases
        if i < 0 or j < 0 or matrix[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1

        # If the result is already computed, return it
        if dp[i][j] != -1:
            return dp[i][j]

        """ Calculate the number of ways by
        moving up and left recursively."""
        up = self.func(i - 1, j, matrix, dp)
        left = self.func(i, j - 1, matrix, dp)

        # Memoize the result and return the total ways
        dp[i][j] = up + left
        return dp[i][j]

    """ Function to find all unique paths to reach
    matrix[m-1][n-1] from matrix[0][0] with obstacles"""
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Initialize DP table to memoize results
        dp = [[-1] * n for _ in range(m)]

        # Return the total number of paths
        return self.func(m - 1, n - 1, matrix, dp)
