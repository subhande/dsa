# 542. 0 1 Matrix
# Distance of nearest cell having 0
# Distance of nearest cell having 1
# 1765: Map of Highest Peak
#TODO: Visit 01 Matrix for other solutions

from collections import deque
from typing import List

# Time Complexity: O(n * m) | Space Complexity: O(n * m)
class Solution:
    # Check if the given row and column are within the bounds of the matrix
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols

    # Main function to find the highest peak in the map
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        # If the map is empty, return an empty list
        if n == 0:
            return []

        # If the entire map is water, return a map with all heights as 0
        if sum([sum(row) for row in isWater]) == n * m:
            return [[0] * m for _ in range(n)]

        # Initialize visited and distance matrices
        visited = [[False] * m for _ in range(n)]
        dist = [[0] * m for _ in range(n)]

        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        queue = deque()
        # Add all water cells to the queue and mark them as visited
        for row in range(n):
            for col in range(m):
                if isWater[row][col] == 1:
                    queue.append((row, col, 0))
                    visited[row][col] = True

        while queue:
            # Pop the front of the queue
            i, j, steps = queue.popleft()

            # Update the distance for the current cell
            dist[i][j] = steps

            # Check all four neighbors
            for (di, dj) in directions:
                ni = i + di
                nj = j + dj
                # Check for valid unvisited neighbors
                if self.isValid(ni, nj, n, m) and not visited[ni][nj]:
                    # If the neighbor is not water, add it to the queue
                    queue.append((ni, nj, steps+1))
                    # Mark the neighbor as visited
                    visited[ni][nj] = True

        return dist
