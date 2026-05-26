# Increment Sub Matrices by One

from typing import List


# Approach 1: Using 1D prefix sum in each row
# Time Complexity: O(q + n^2) where q is the number of queries and n is the size of the matrix | Space Complexity: O(n^2) where n is the size of the matrix
#
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        for query in queries:
            r1, c1, r2, c2 = query
            for r in range(r1, r2 + 1):
                matrix[r][c1] += 1
                if c2 + 1 < n:
                    matrix[r][c2 + 1] -= 1

        for i in range(n):
            runningSum = 0
            for j in range(n):
                runningSum += matrix[i][j]
                matrix[i][j] = runningSum

        return matrix


# Approach 2: Using 2D prefix sum
# Time Complexity: O(q + n^2) where q is the number of queries and n is the size of the matrix | Space Complexity: O(n^2) where n is the size of the matrix
# REf: https://www.youtube.com/watch?v=qO3TKLlvqas
class Solution2:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else mat[i - 1][j]
                x2 = 0 if j == 0 else mat[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
                mat[i][j] = diff[i][j] + x1 + x2 - x3
        return mat
