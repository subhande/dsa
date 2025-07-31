# 542. 0 1 Matrix
# Distance of nearest cell having 0
# Distance of nearest cell having 1
# 1765: Map of Highest Peak

from collections import deque
from typing import List

# Distance of nearest cell having 0 | Multi-source BFS | Start from 0s
class Solution1:
    def isValid(self, row: int, col: int, rows: int, cols: int) -> bool:
        return 0 <= row < rows and 0 <= col < cols

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Number of rows and columns
        n = len(mat)
        if n == 0:
            return []
        m = len(mat[0])

        # If the mat contains only 0s, return the mat
        matSum = sum([sum(row) for row in mat])
        if matSum == 0:
            return mat

        # Create a distance mat, initialize with 0
        dist = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        q = deque()

        # Add all 0s to the queue and mark them as visited
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j, 0))
                    visited[i][j] = True
                else:
                    visited[i][j] = False

        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Perform multi-source BFS
        while q:
            i, j, steps = q.popleft()
            # Update the distance of itself
            dist[i][j] = steps
            # Check all four neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # check for valid unvisited neighbors
                if self.isValid(ni, nj, n, m) and not visited[ni][nj]:
                    q.append((ni, nj, steps + 1))
                    visited[ni][nj] = True
        return dist



# Using DP | Distance of nearest cell having 1 | Two-pass DP approach | Start from 1s
class Solution2:
    def nearest(self, grid):
        if not grid:
            return []

        # If the grid contains only 0s, return the grid
        gridSum = sum([sum(row) for row in grid])
        if gridSum == 0:
            return grid

        n, m = len(grid), len(grid[0])
        # Initialize DP with a large number.
        dp = [[float('inf')] * m for _ in range(n)]

        # First pass: top-left to bottom-right.
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # Look top.
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    # Look left.
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        # Second pass: bottom-right to top-left.
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Look bottom.
                if i < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                # Look right.
                if j < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)

        return dp
