# Grid Unique Paths
# https://takeuforward.org/plus/dsa/dynamic-programming/dp-on-grids/grid-unique-paths


class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
