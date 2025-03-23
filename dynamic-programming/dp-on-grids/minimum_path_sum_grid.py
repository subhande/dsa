
# Minimum Path SUm Grid


class Solution:
    def minFallingPathSumSpaceOptimized(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # Use a single array to store the previous row's values
        prev = matrix[0]

        # Iterate over each row starting from the second
        for row in range(1, rows):
            # Create a new array for the current row
            curr = [float('inf')] * cols
            for col in range(cols):
                # Get the minimum value from the previous row (down, down-left, down-right)
                down = prev[col]
                down_left = prev[col - 1] if col - 1 >= 0 else float('inf')
                down_right = prev[col + 1] if col + 1 < cols else float('inf')

                # Update the current row array with the current cell value plus the minimum above
                curr[col] = matrix[row][col] + min(down, down_left, down_right)
            # Move to the next row by setting prev to curr
            prev = curr

        # Return the minimum value from the last row array
        return min(prev)
