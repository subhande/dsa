# Number of Distinct Islands
from typing import List
from collections import deque
class Solution:
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    def bfs(self, r, c, rows, cols, grid):
        queue = deque()
        queue.append((r, c, 0, 0))
        grid[r][c] = 0
        path = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, rrow, rcol = queue.popleft()
            path.append((rrow, rcol))
            for dr, dc in directions:
                nrow = row + dr
                ncol = col + dc
                nrrow = rrow + dr
                nrcol = rcol + dc
                if self.isValid(nrow, ncol, rows, cols) and grid[nrow][ncol] == 1:
                    queue.append((nrow, ncol, nrrow, nrcol))
                    grid[nrow][ncol] = 0
        return tuple(path) if path else None


    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        landAreaMap = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    landArea = self.bfs(row, col, rows, cols, grid)
                    if landArea:
                        landAreaMap.add(landArea)
        return len(landAreaMap)

if __name__ == "__main__":
    s = Solution()
    test_cases = [{
        "grid": [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        "output": 1
    },{
        "grid": [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
,
        "output": 3
    },
    {
        "grid": [[0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],[0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],[1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]

,
        "output": 15
    }]

    for t in test_cases:
        grid = t["grid"]
        output = t["output"]
        print(f"Input: grid = {grid}")
        print(f"Output: {s.numDistinctIslands(grid)} | Expected: {output}\n")
