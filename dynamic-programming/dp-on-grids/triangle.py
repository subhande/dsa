# Triangle


```class Solution:
    def minTriangleSum(self, triangle):
        """
        Function to calculate the minimum falling path sum from the first row to the last
        in a triangle array.

        :param triangle: 2D list of integers where each row has one more element than the previous.
        :return: Minimum falling path sum.
        """
        # Number of rows in the triangle
        num_rows = len(triangle)

        # Number of columns in the triangle
        num_cols = len(triangle[-1])

        # Initialize a list to store the minimum path sums of the previous row
        # Using infinity for initialization to handle edge cases
        prev_row_min_sums = [float("inf") for _ in range(num_cols)]

        # The minimum path sum for the first row is just the first element
        prev_row_min_sums[0] = triangle[0][0]

        # Iterate over each row starting from the second row
        for row in range(1, num_rows):

            # Create a new list to store the minimum path sums for the current row
            curr_row_min_sums = [float("inf") for _ in range(num_cols)]

            # Update the first element in the current row
            curr_row_min_sums[0] = prev_row_min_sums[0] + triangle[row][0]

            # Update the rest of the elements in the current row
            for col in range(1, row + 1):
                current_value = triangle[row][col]

                # Calculate the minimum path sum for the current element
                curr_row_min_sums[col] = min(
                    prev_row_min_sums[col] + current_value,     # From the element directly above
                    prev_row_min_sums[col - 1] + current_value # From the element above-left
                )

            # Update the previous row's minimum sums with the current row's sums
            prev_row_min_sums = curr_row_min_sums

        # Return the minimum value in the last row's minimum sums
        return min(prev_row_min_sums)
```
