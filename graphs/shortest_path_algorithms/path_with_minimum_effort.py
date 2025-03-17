# Path With Minimum Effort
# https://takeuforward.org/plus/dsa/graph/shortest-path-algorithms/path-with-minimum-effort


import heapq
class Solution:
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    def MinimumEffort(self, grid):
        rows, cols = len(grid), len(grid[0])
        source = (0, 0)
        destination = (rows - 1, cols - 1)

        if source == destination:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]



        effort = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        effort[source[0]][source[1]] = 0

        minHeap = [(0, source[0], source[1])]

        while minHeap:
            absDiff, row, col = heapq.heappop(minHeap)
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if self.isValid(newRow, newCol, rows, cols):
                    newEffort = max(absDiff, abs(grid[row][col] - grid[newRow][newCol]))
                    if newEffort < effort[newRow][newCol]:
                        effort[newRow][newCol] = newEffort
                        heapq.heappush(minHeap, (newEffort, newRow, newCol))

        return effort[-1][-1]
