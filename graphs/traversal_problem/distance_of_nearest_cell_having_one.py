# Number of distinct islands

"""
Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.

The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.
"""

from collections import deque

class Solution:

    def isValid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m

    def nearest(self, grid):
        # Number of rows and columns
        n = len(grid)
        if n == 0:
            return []
        m = len(grid[0])

        # If the grid contains only 0s, return the grid
        gridSum = sum([sum(row) for row in grid])
        if gridSum == 0:
            return grid
        # Create a distance grid, initialize with a large number
        dist = [[float('inf')] * m for _ in range(n)]
        q = deque()

        # Add all cells with 1 to the queue with distance 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Perform multi-source BFS
        while q:
            i, j = q.popleft()
            # Check all four neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # If we find a shorter path from the neighbor, update it.
                if self.isValid(ni, nj, n, m) and dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))

        return dist

class Solution2:

    def isValid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m

    def nearest(self, grid):
        # Number of rows and columns
        n = len(grid)
        if n == 0:
            return []
        m = len(grid[0])

        # If the grid contains only 0s, return the grid
        gridSum = sum([sum(row) for row in grid])
        if gridSum == 0:
            return grid
        # Create a distance grid, initialize with 0
        dist = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        q = deque()

        # Add all cells with 1 to the queue with distance 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
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

class Solution3:
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

if __name__ == '__main__':
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()

    grid = [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]
    print(sol1.nearest(grid)) # [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]
    print(sol2.nearest(grid)) # [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]
    print(sol3.nearest(grid)) # [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]

    grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]
    print(sol1.nearest(grid)) # [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
    print(sol2.nearest(grid)) # [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
    print(sol3.nearest(grid)) # [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
