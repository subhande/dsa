# Longest Increasing Path
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/?envType=company&envId=google&favoriteSlug=google-thirty-days



# Solution 1: Own Solution | Slightly different from the actual solution bottom up approach
class Solution1:
    def isValid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m
    def dfs(self, r, c, n, m, matrix, dp, max_seq):
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        dp[r][c] = max(dp[r][c], 1)
        stack = [(r, c, dp[r][c])]
        while stack:
            row, col, count = stack.pop()
            max_seq[0] = max(max_seq[0], count)
            for (dr, dc) in dir:
                nr = row + dr
                nc = col + dc
                if self.isValid(nr, nc, n, m) and matrix[nr][nc] > matrix[row][col] and count + 1 > dp[nr][nc]:
                    stack.append((nr, nc, count+1))
                    dp[nr][nc] = count+1
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        max_seq = [1]
        for r in range(n):
            for c in range(m):
                if dp[r][c] == -1:
                    self.dfs(r, c, n, m, matrix, dp, max_seq)
        return max_seq[0]

# Solution 2: Top Down Approach

class Solution2:
    def dfs(self, i: int, j: int, n: int, m: int, dp: list[list[int]], directions: list[tuple[int, int]], matrix: list[list[int]]) -> int:
        """
        Perform a depth-first search starting from cell (i, j) to find the longest increasing path.
        Uses memoization to avoid redundant calculations.
        """
        # If we have already computed the longest path from (i, j), return it.
        if dp[i][j]:
            return dp[i][j]

        # Initialize the maximum path length from (i, j) as 1 (the cell itself).
        max_path = 1

        # Explore all four directions.
        for dx, dy in directions:
            x, y = i + dx, j + dy
            # Check if the new cell is within bounds and its value is greater than the current cell's value.
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                # Recursively get the length of the path from the neighbor and add 1 for the current cell.
                length = 1 + self.dfs(x, y, n, m, dp, directions, matrix)
                # Update the maximum path length found so far.
                max_path = max(max_path, length)

        # Store the computed longest path length in the memoization table.
        dp[i][j] = max_path
        return max_path

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # Edge case: if the matrix is empty, return 0.
        if not matrix or not matrix[0]:
            return 0

        # Get the dimensions of the matrix.
        m, n = len(matrix), len(matrix[0])

        # Create a memoization table (dp) with the same dimensions as the matrix.
        # Each entry dp[i][j] will store the length of the longest increasing path starting from cell (i, j).
        dp = [[0] * n for _ in range(m)]

        # Directions for moving in the matrix: down, up, right, and left.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Iterate over every cell in the matrix to find the overall longest increasing path.
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, self.dfs(i, j, n, m, dp, directions, matrix))

        return result


if __name__ == "__main__":
    sol1 = Solution1()
    sol2 = Solution2()

    # Test 1
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    expectedOutput = 4
    assert sol1.longestIncreasingPath(matrix) == expectedOutput
    assert sol2.longestIncreasingPath(matrix) == expectedOutput

    # Test 2
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    expectedOutput = 4
    assert sol1.longestIncreasingPath(matrix) == expectedOutput
    assert sol2.longestIncreasingPath(matrix) == expectedOutput
