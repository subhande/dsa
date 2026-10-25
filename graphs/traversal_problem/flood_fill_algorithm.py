# Flood Fill Algorithm
from collections import deque

## DFS SOlution

class Solution:
    def isValid(self, r, c, rows, cols):
        # Check if the coordinates are within bounds
        return 0 <= r < rows and 0 <= c < cols

    def bfs(self, r, c, rows, cols, grid, original_color, new_color):
        queue = deque()
        queue.append((r, c))
        # Mark the current cell as visited
        grid[r][c] = new_color

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if self.isValid(nr, nc, rows, cols) and grid[nr][nc] == original_color:
                    grid[nr][nc] = new_color
                    queue.append((nr, nc))

    # Time Complexity: O(n*m) | Space Complexity: O(n*m)
    def floodFill(self, image, sr, sc, newColor):
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]
        if original_color == newColor:
            return image

        self.bfs(sr, sc, rows, cols, image, original_color, newColor)
        return image

## BFS Solution

class Solution:

    def isValid(self, r, c, rows, cols) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    def dfs(self, r, c, rows, cols, grid, original_color, new_color):

        stack = []
        stack.append((r, c))

        grid[r][c] = new_color

        while stack:

            row, col = stack.pop()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if self.isValid(nr, nc, rows, cols) and grid[nr][nc] == original_color:
                    grid[nr][nc] = new_color
                    stack.append((nr, nc))

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]
        
        if original_color == color:
            return image

        self.dfs(sr, sc, rows, cols, image, original_color, color)

        return image

        
        

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(sol.floodFill(image, sr, sc, newColor))  # Output: [[2,2,2],[2,2,0],[2,0,1]]

    # Test 2
    image = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
    sr = 2
    sc = 2
    newColor = 3
    print(sol.floodFill(image, sr, sc, newColor))  # Output: [[0,1,0],[1,1,0],[0,0,3]]
