# Shortest Distance in a Binary Maze
# https://takeuforward.org/plus/dsa/graph/shortest-path-algorithms/shortest-path-with-minimum-effort
from collections import deque
class Solution:
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    def shortestPath(self, grid, source, destination):
        if source == destination:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows, cols = len(grid), len(grid[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        dist[source[0]][source[1]] = 0

        queue = deque([(0, source[0], source[1])])

        while queue:
            distance, row, col = queue.popleft()
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if self.isValid(newRow, newCol, rows, cols) and grid[newRow][newCol] == 1 and distance + 1 < dist[newRow][newCol]:
                    dist[newRow][newCol] = distance + 1

                    if (newRow, newCol) == destination:
                        return distance + 1

                    queue.append((distance + 1, newRow, newCol))

        return -1

import heapq
class Solution2:
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    def shortestPath(self, grid, source, destination):
        if source == destination:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows, cols = len(grid), len(grid[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        dist[source[0]][source[1]] = 0

        minHeap = [(0, source[0], source[1])]

        while minHeap:
            distance, row, col = heapq.heappop(minHeap)
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if self.isValid(newRow, newCol, rows, cols) and grid[newRow][newCol] == 1 and distance + 1 < dist[newRow][newCol]:
                    dist[newRow][newCol] = distance + 1

                    if (newRow, newCol) == destination:
                        return distance + 1

                    heapq.heappush(minHeap, (distance + 1, newRow, newCol))

if __name__ == '__main__':
    sol = Solution()
    sol1 = Solution2()

    # Test 1
    grid = [[1, 1, 1, 1],[1, 1, 0, 1],[1, 1, 1, 1],[1, 1, 0, 0],[1, 0, 0, 1]]
    source = (0, 1)
    destination = (2, 2)
    print(sol.shortestPath(grid, source, destination))  # Expected output: 3
    print(sol1.shortestPath(grid, source, destination))  # Expected output: 3
