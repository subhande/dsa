# Making a large Island
# https://leetcode.com/problems/making-a-large-island/description/

from typing import List

class DisjoinSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def findParent(self, u: int) -> int:
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)


class Solution:
    def isValid(self, row: int, col: int, rows: int, cols: int) -> bool:
        return 0 <= row < rows and 0 <= col < cols

    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Initialize DSU for the entire grid
        ds = DisjoinSet(rows * cols)

        # Direction vectors for traversing up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Union adjacent `1`s in the grid
        for curr_row in range(rows):
            for curr_col in range(cols):
                if grid[curr_row][curr_col] == 1:
                    # Flatten 2D index to 1D
                    current_node = (cols * curr_row) +  curr_col

                    for direction in directions:
                        nrow = curr_row + direction[0]
                        ncol = curr_col + direction[1]
                        # Check bounds and ensure the neighbor is also `1`
                        if self.isValid(nrow, ncol, rows, cols) and grid[nrow][ncol] == 1:
                            nnode = (cols * nrow) +  ncol
                            ds.union(current_node, nnode)


        # Step 2: Calculate the maximum possible island size
        max_island_size = 0

        # Flag to check if there are any zeros in the grid
        has_zero = False

        # To store unique roots for a `0`'s neighbors
        unique_roots = set()


        for curr_row in range(rows):
            for curr_col in range(cols):
                if grid[curr_row][curr_col] == 0:
                    has_zero = True

                    # Start with the flipped `0`
                    current_island_size = 1

                    for direction in directions:
                        nrow = curr_row + direction[0]
                        ncol = curr_col + direction[1]

                        # Check bounds and ensure the neighbor is `1`
                        if self.isValid(nrow, ncol, rows, cols) and grid[nrow][ncol] == 1:
                            nnode = (cols * nrow) +  ncol
                            parent = ds.findParent(nnode)
                            unique_roots.add(parent)


                    # Sum up the sizes of unique neighboring islands
                    for root in unique_roots:
                        current_island_size += ds.size[root]

                    # Clear the set for the next `0`
                    unique_roots.clear()

                    # Update the result with the largest island size found
                    max_island_size = max(max_island_size, current_island_size)

        # If there are no zeros, the largest island is the entire grid
        if not has_zero:
            return rows * cols
        return max_island_size
