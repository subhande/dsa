# Cherry Pickup
# https://leetcode.com/problems/cherry-pickup/description/

"""

r, c, r1, c1

r1 + c1 = r2 + c2
r2 = r1 + c1 - c2

"""

from typing import List
class Solution:
    def cherryPickupRecursiveMemoization(self, grid: List[List[int]], r1: int, c1: int, c2: int, n: int, m: int, memo: List[List[List[int]]]) -> int:
        NINF = - 10**9
        r2 = r1 + c1 - c2
        if r1 >= n or c1 >= m or r2 >= n or c2 >= m or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return NINF

        if r1 == n - 1 and c1 == m - 1:
            return grid[r1][c1]

        if memo[r1][c1][c2] != -1:
            return memo[r1][c1][c2]

        ans = grid[r1][c1]
        if c1 != c2:
            ans += grid[r2][c2]

        ans += max(
            self.cherryPickupRecursiveMemoization(grid, r1 + 1, c1, c2, n, m, memo), # down down
            self.cherryPickupRecursiveMemoization(grid, r1 + 1, c1, c2 + 1, n, m, memo), # down right
            self.cherryPickupRecursiveMemoization(grid, r1, c1 + 1, c2, n, m, memo), # right down
            self.cherryPickupRecursiveMemoization(grid, r1, c1 + 1, c2 + 1, n, m, memo) # right right
        )

        memo[r1][c1][c2] = ans

        return ans

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = [[[-1] * m for _ in range(m)] for _ in range(n)]
        return max(0, self.cherryPickupRecursiveMemoization(grid, 0, 0, 0, n, m, memo))


if __name__ == "__main__":
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    sol = Solution()
    print(sol.cherryPickup(grid))  # Output: 5
    grid = [[1, 1, -1], [1, 0, -1], [1, 1, 1]]
    print(sol.cherryPickup(grid))  # Output: 6
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(sol.cherryPickup(grid))  # Output: 2
    grid = [[1]]
    print(sol.cherryPickup(grid))  # Output: 1
