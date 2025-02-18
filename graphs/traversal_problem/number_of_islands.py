# Number of Islands

from collections import deque

class Solution:
    def isValid(self, r, c, rows, cols):
        # Check if the coordinates are within bounds
        return 0 <= r < rows and 0 <= c < cols

    def bfs(self, r, c, rows, cols, visited, grid):
        visited[r][c] = True

        queue = deque()
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = row + dr, col + dc
                    if self.isValid(nr, nc, rows, cols) and not visited[nr][nc] and grid[nr][nc] == '1':
                        visited[nr][nc] = True
                        queue.append((nr, nc))

    # Time Complexity: O(n*m) | Space Complexity: O(n*m)
    def numIslands(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        no_of_islands = 0

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == '1':
                    no_of_islands += 1
                    self.bfs(r, c, rows, cols, visited, grid)
        return no_of_islands


class Solution2:
    def isValid(self, r, c, rows, cols):
        # Check if the coordinates are within bounds
        return 0 <= r < rows and 0 <= c < cols

    def bfs(self, r, c, rows, cols, grid):
        queue = deque()
        queue.append((r, c))
        # Mark the current cell as visited
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = row + dr, col + dc
                    if self.isValid(nr, nc, rows, cols) and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

    # Time Complexity: O(n*m) | Space Complexity: O(1)
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                # If the cell is part of an island
                if grid[i][j] == '1':
                    num_islands += 1
                    self.bfs(i, j, rows, cols, grid)
        return num_islands

if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()

    # Example 1
    grid = [ ["1", "1", "1", "0", "1"], ["1", "0", "0", "0", "0"], ["1", "1", "1", "0", "1"], ["0", "0", "0", "1", "1"] ]

    print(sol.numIslands(grid)) # Output: 2
    print(sol2.numIslands(grid)) # Output: 2


    # Example 2
    grid =  [ ["1", "0", "0", "0", "1"], ["0", "1", "0", "1", "0"], ["0", "0", "1", "0", "0"], ["0", "1", "0", "1"," 0"] ]

    print(sol.numIslands(grid)) # Output: 1
    print(sol2.numIslands(grid)) # Output: 1
