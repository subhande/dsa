# Rotten Oranges

"""
Given an n x m grid, where each cell has the following values :
2 - represents a rotten orange
1 - represents a Fresh orange
0 - represents an Empty Cell

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten.

Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.
"""

from collections import deque
class Solution:

    def isValid(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols


    def orangesRotting(self, grid):

        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: gather all initially rotten oranges and count fresh ones.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minuteLevel)
                elif grid[r][c] == 1:
                    fresh_count += 1
        # This will track the maximum number of minutes needed.
        max_minutes = 0

        # Define 4-direction moves.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS(level order)
        while queue:
            row, col, minutes = queue.popleft()
            max_minutes = max(max_minutes, minutes)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if self.isValid(nr, nc, rows, cols) and grid[nr][nc] == 1:
                    # Infect the fresh orange.
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))

        # If there are still fresh oranges left, it's impossible.
        return max_minutes if fresh_count == 0 else -1



if __name__ == "__main__":
    sol = Solution()

    # Test 1
    grid =  [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]
    print(sol.orangesRotting(grid))  # Output: -1

    # Test 2
    grid =  [ [2,1,1] , [1,1,0] , [0,1,1] ]
    print(sol.orangesRotting(grid))  # Output: 4

    # Test 3
    grid = [[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0]]

    print(sol.orangesRotting(grid))  # Output: 3
