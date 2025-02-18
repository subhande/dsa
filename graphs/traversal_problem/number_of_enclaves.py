# Number Of Enclaves

from collections import deque

class Solution:
    def isValid(self, r, c, n_rows, n_cols):
        return 0 <= r < n_rows and 0 <= c < n_cols

    def isBoundary(self, r, c, n_rows, n_cols):
        return r == 0 or r == n_rows - 1 or c == 0 or c == n_cols - 1

    def bfs(self, r, c, n_rows, n_cols, grid):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = 0  # Mark as visited

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr = row + dr
                nc = col + dc
                if self.isValid(nr, nc, n_rows, n_cols) and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = 0  # Mark neighbor as visited

    # Time Complexity: O(n*m) | Space Complexity: O(n*m)
    def numberOfEnclaves(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and self.isBoundary(r, c, n_rows, n_cols):
                    self.bfs(r, c, n_rows, n_cols, grid)
        enclave_count = 0
        for row in grid:
            enclave_count += sum(row)
        return enclave_count

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(sol.numberOfEnclaves(grid)) # Output: 3

    # Test 2
    grid =  [[0, 0, 0, 1],[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(sol.numberOfEnclaves(grid)) # Output: 3
