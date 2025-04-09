# Cherry Pickeup II
# https://leetcode.com/problems/cherry-pickup-ii/

from typing import List
class Solution:
    def cherryPickupRecursiveMemoization(self, grid: List[List[int]], r: int, c1: int, c2: int, n: int, m: int, memo: List[List[List[int]]]) -> int:
        NINF = int(-10e9)
        if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m:
            return NINF

        if r == n - 1:
            if c1 == c2:
                return grid[r][c1]
            else:
                return grid[r][c1] + grid[r][c2]

        if memo[r][c1][c2] != -1:
            return memo[r][c1][c2]

        ans = grid[r][c1]
        if c1 != c2:
            ans += grid[r][c2]

        res = 0
        # Move down, down-left and down-right
        for i in range(-1, 2):
            for j in range(-1, 2):
                res = max(res, self.cherryPickupRecursiveMemoization(grid, r + 1, c1 + i, c2 + j, n, m, memo))
        ans += res
        memo[r][c1][c2] = ans

        return ans

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = [[[-1] * m for _ in range(m)] for _ in range(n)]
        return self.cherryPickupRecursiveMemoization(grid, 0, 0, m-1, n, m, memo)
