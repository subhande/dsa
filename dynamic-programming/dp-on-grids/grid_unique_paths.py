# Grid Unique Paths
# https://takeuforward.org/plus/dsa/dynamic-programming/dp-on-grids/grid-unique-paths

from typing import List

class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]

class Solution2:
    def uniquePathsHelper(self, m: int, n: int, memo: List[List[int]]):
        if m == 0 or n == 0:
            return 1
        if memo[m][n] != -1:
            return memo[m][n]
        memo[m][n] = self.uniquePathsHelper(m - 1, n, memo) + self.uniquePathsHelper(m, n - 1, memo)
        return memo[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.uniquePathsHelper(m - 1, n - 1, memo)


class Solution3:
    def uniquePathsHelper(self, m: int, n: int, memo: List[List[int]]):
        if m < 0 or n < 0:
            return 0
        if m == 0 and n == 0:
            return 1
        if memo[m][n] != -1:
            return memo[m][n]
        memo[m][n] = self.uniquePathsHelper(m - 1, n, memo) + self.uniquePathsHelper(m, n - 1, memo)
        return memo[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.uniquePathsHelper(m - 1, n - 1, memo)
