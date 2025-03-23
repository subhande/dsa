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
